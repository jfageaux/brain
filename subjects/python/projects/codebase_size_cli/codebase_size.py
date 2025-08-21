"""
Codebase Size CLI - Measure how much space your codebase uses on disk.

This script walks through a directory (by default, the current directory)
and calculates the total size of files. It provides several helpful outputs:

1) Total size in a human-readable format (e.g., MB/GB)
2) Optional breakdown by file extension (useful to see where space goes)
3) Optional list of the largest N files
4) Optional JSON output for use in other tools

Why this project?
- This is a great first CLI because it touches core Python skills:
  - file system traversal (os, pathlib)
  - argument parsing (argparse)
  - error handling (permissions, broken links)
  - formatting results (human vs JSON)

Design choices (explained simply):
- We default to ignoring common "noise" directories (e.g., .git, __pycache__,
  virtual environments) so results focus on your actual project files.
- We use os.scandir for efficient directory walking on all platforms
  (including Windows, which you're using), with clear try/except guards.
- We separate logic into small functions with docstrings, so each piece is
  easy to test, understand, and reuse.

Usage examples (PowerShell on Windows):
  # Measure current folder
  python subjects\\python\\projects\\codebase_size_cli\\codebase_size.py

  # Measure a specific path (brain repository root, if you're elsewhere)
  python subjects\\python\\projects\\codebase_size_cli\\codebase_size.py --path .

  # Include a breakdown by file extension and show top 10 largest files
  python subjects\\python\\projects\\codebase_size_cli\\codebase_size.py --by-ext --top 10

  # Output as JSON (machine-readable)
  python subjects\\python\\projects\\codebase_size_cli\\codebase_size.py --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Set, Tuple


# ------------------------------ Data Structures ------------------------------


@dataclass
class FileInfo:
    """Simple container for file metadata we care about.

    Attributes:
        path: Absolute or relative path to the file.
        size_bytes: File size in bytes.
        extension: Lowercased file extension (e.g., ".py"). Empty string if none.
    """

    path: str
    size_bytes: int
    extension: str


# ------------------------------ Helper Functions -----------------------------


def human_readable_size(num_bytes: int) -> str:
    """Convert raw bytes to a human-friendly string.

    We scale using powers of 1024 (KiB, MiB, GiB) which is common in tooling.
    Example: 1_234_567 bytes -> "1.18 MiB"
    """

    # Define the units in ascending order; we will iterate until we fit nicely
    units = ["bytes", "KiB", "MiB", "GiB", "TiB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            # Format with two decimals for readability
            if unit == "bytes":
                return f"{int(size)} {unit}"
            return f"{size:.2f} {unit}"
        size /= 1024.0
    # Fallback (should never hit due to return inside loop)
    return f"{num_bytes} bytes"


def default_excluded_dirs() -> Set[str]:
    """Common directories to skip by default.

    Rationale: These directories frequently contain binary caches or third-party
    dependencies that do not represent your authored code and can distort size
    measurements if included.
    """

    return {
        ".git",
        "__pycache__",
        "node_modules",
        "venv",
        ".venv",
        "env",
        "build",
        "dist",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
    }


def iter_files(
    root: Path,
    excluded_dirs: Set[str],
    include_hidden: bool,
    follow_symlinks: bool,
) -> Iterator[Path]:
    """Yield paths for all regular files under `root`.

    We use os.scandir for performance and to minimize system calls. Hidden files
    on Windows don't always start with a dot, but for simplicity we treat "dot"
    names as hidden across platforms. You can override with --include-hidden.
    """

    # Use a manual stack to avoid recursion limits on very deep trees
    stack: List[Path] = [root]

    while stack:
        current = stack.pop()

        try:
            with os.scandir(current) as it:
                for entry in it:
                    try:
                        # Skip hidden (dot) entries unless explicitly requested
                        name = entry.name
                        if not include_hidden and name.startswith("."):
                            if entry.is_dir(follow_symlinks=False):
                                # Do not traverse into hidden directory
                                continue
                            # Skip hidden file
                            continue

                        # Skip excluded directories by name match (shallow check)
                        if entry.is_dir(follow_symlinks=follow_symlinks):
                            if name in excluded_dirs:
                                continue
                            # Add directory to stack for traversal
                            stack.append(Path(entry.path))
                            continue

                        # Only yield regular files; ignore others (sockets, devices)
                        if entry.is_file(follow_symlinks=follow_symlinks):
                            yield Path(entry.path)
                    except (PermissionError, FileNotFoundError):
                        # Some entries may become inaccessible or disappear; skip
                        continue
        except (PermissionError, FileNotFoundError):
            # Current directory might be inaccessible; skip
            continue


def collect_file_info(paths: Iterable[Path]) -> Iterator[FileInfo]:
    """Map raw Path objects to FileInfo with size and extension.

    We keep errors localized; unreadable files are skipped gracefully.
    """

    for path in paths:
        try:
            size = path.stat().st_size
            ext = path.suffix.lower()  # ".py", ".md", or "" if none
            yield FileInfo(path=str(path), size_bytes=size, extension=ext)
        except (PermissionError, FileNotFoundError, OSError):
            # If file vanishes or can't be read, we skip it
            continue


def summarize_by_extension(files: Iterable[FileInfo]) -> Dict[str, int]:
    """Return a dict mapping file extension -> total size in bytes.

    Empty-extension files are grouped under "<no_ext>" to avoid empty keys.
    """

    totals: Dict[str, int] = defaultdict(int)
    for info in files:
        key = info.extension if info.extension else "<no_ext>"
        totals[key] += info.size_bytes
    return dict(totals)


def top_n_largest(files: Iterable[FileInfo], n: int) -> List[FileInfo]:
    """Return the N largest files, sorted descending by size.

    We convert to a list to avoid re-iterating generators multiple times.
    """

    items = list(files)
    items.sort(key=lambda f: f.size_bytes, reverse=True)
    return items[:n]


# --------------------------------- CLI Logic ---------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for our CLI.

    We expose flags that let you customize traversal and output formatting.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Measure how much space your codebase uses on disk. "
            "By default, common cache and dependency directories are excluded."
        )
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help=(
            "The directory to measure. Defaults to current directory. "
            "You can pass an absolute or relative path."
        ),
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include dot-directories and dot-files (e.g., .git, .vscode)",
    )
    parser.add_argument(
        "--follow-symlinks",
        action="store_true",
        help="Follow symbolic links while traversing (can be slower or circular)",
    )
    parser.add_argument(
        "--no-default-excludes",
        action="store_true",
        help="Do not exclude common cache/dependency directories by default",
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help=(
            "Additional directory names to exclude (exact name match). "
            "Example: --exclude .vscode coverage"
        ),
    )
    parser.add_argument(
        "--by-ext",
        action="store_true",
        help="Show a breakdown by file extension",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="Show the N largest files (0 to disable)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of human-readable text",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """Entry point for the CLI.

    We parse flags, traverse the file tree, compute totals, and print either
    human-readable or JSON output based on user preference.
    """

    parser = build_parser()
    args = parser.parse_args(argv)

    # Resolve and validate the target path
    target_path = Path(args.path).resolve()
    if not target_path.exists() or not target_path.is_dir():
        print(f"Error: path does not exist or is not a directory: {target_path}", file=sys.stderr)
        return 2

    # Build the set of excluded directory names
    excluded = set(args.exclude)
    if not args.no_default_excludes:
        excluded |= default_excluded_dirs()

    # 1) Traverse file system and collect file info
    file_paths = iter_files(
        root=target_path,
        excluded_dirs=excluded,
        include_hidden=args.include_hidden,
        follow_symlinks=args.follow_symlinks,
    )
    files_list = list(collect_file_info(file_paths))

    # 2) Compute total size
    total_size_bytes = sum(f.size_bytes for f in files_list)

    # 3) Optional breakdowns
    by_ext: Optional[Dict[str, int]] = None
    if args.by_ext:
        by_ext = summarize_by_extension(files_list)

    top_files: Optional[List[FileInfo]] = None
    if args.top and args.top > 0:
        top_files = top_n_largest(files_list, args.top)

    # 4) Output
    if args.json:
        # JSON-friendly structure
        output = {
            "path": str(target_path),
            "total_size_bytes": total_size_bytes,
            "total_size_human": human_readable_size(total_size_bytes),
            "excluded_dirs": sorted(list(excluded)),
            "include_hidden": bool(args.include_hidden),
            "follow_symlinks": bool(args.follow_symlinks),
        }
        if by_ext is not None:
            output["by_extension_bytes"] = dict(sorted(by_ext.items(), key=lambda kv: kv[1], reverse=True))
        if top_files is not None:
            output["top_files"] = [
                {
                    "path": f.path,
                    "size_bytes": f.size_bytes,
                    "size_human": human_readable_size(f.size_bytes),
                    "extension": f.extension,
                }
                for f in top_files
            ]
        print(json.dumps(output, indent=2))
        return 0

    # Human-readable text output
    print(f"Path: {target_path}")
    print(f"Excluded directories: {', '.join(sorted(list(excluded))) or '(none)'}")
    print(f"Include hidden: {'yes' if args.include_hidden else 'no'} | Follow symlinks: {'yes' if args.follow_symlinks else 'no'}")
    print("")
    print(f"Total size: {human_readable_size(total_size_bytes)} ({total_size_bytes} bytes)")

    if by_ext is not None:
        print("\nBreakdown by file extension (largest first):")
        for ext, size in sorted(by_ext.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {ext:>8}: {human_readable_size(size)} ({size} bytes)")

    if top_files is not None and len(top_files) > 0:
        print(f"\nTop {len(top_files)} largest files:")
        for f in top_files:
            print(f"  {human_readable_size(f.size_bytes):>12}  {f.path}")

    return 0


if __name__ == "__main__":
    # Delegate to main() so we can test/import cleanly
    raise SystemExit(main())


