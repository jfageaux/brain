"""
Outlook + Invoice Workflow Helper (CLI Skeleton)
================================================

This CLI is designed to support day-to-day maritime operations tasks while following
the "comment-driven development" approach. The goal is to start with safe, read-only
utilities, then gradually add automation once behavior is well-understood and tested.

Subcommands (planned):
  - parse-emails:    Read exported Outlook emails and extract structured fields
  - gen-checklist:   Generate markdown checklists from parsed email data
  - validate-invoices: Validate CSV/Excel data before entry into COSCO system

Safety Principle:
  - Start read-only; operate only on exported files in a sandbox directory
  - Produce transparent, auditable outputs (JSONL, CSV, Markdown reports)

You can run this file directly with Python. See the README in this project folder for
example usage. All functions here are heavily commented to explain the reasoning
and design decisions at a level suitable for someone with ~1 year of CS background.
"""

from __future__ import annotations

import argparse  # For parsing command-line arguments
import json      # For emitting structured output (JSON/JSONL)
import sys       # For process exit codes and stdout/stderr
from pathlib import Path  # For robust, cross-platform filesystem paths


def ensure_directory_exists(path: Path) -> None:
    """
    Ensure the parent directory of a file path exists.

    Why this function exists:
    - Many commands will write outputs (JSONL, Markdown). To avoid runtime errors,
      we create the directory tree first. This is safe and idempotent.
    """
    if path.suffix:
        # If a file path was provided (has an extension), create its parent folder
        path.parent.mkdir(parents=True, exist_ok=True)
    else:
        # If a directory path was provided, create it directly
        path.mkdir(parents=True, exist_ok=True)


def parse_emails_command(input_dir: Path, output_file: Path) -> int:
    """
    Parse exported Outlook emails (read-only) and emit JSON Lines.

    Parameters
    - input_dir: Directory containing exported emails (.eml/.msg/.txt). We will keep
      the parsing very conservative at first (placeholder). Later we can add robust
      parsers once we know the exact formats you can export.
    - output_file: JSONL file path to write one JSON object per email.

    Behavior (initial stub):
    - Walk the input directory and list candidate files by extension
    - For now, we DO NOT parse content in detail; we emit a placeholder record with
      filename and path. This ensures the end-to-end flow works and provides a place
      to plug in real parsing rules later without changing the CLI surface.
    """
    # Define which file extensions we consider as email exports at this stage.
    # We will refine this based on the actual formats you provide (e.g., .msg/.eml/.txt).
    candidate_exts = {".eml", ".msg", ".txt"}

    # Prepare output destination and ensure parent folder exists
    ensure_directory_exists(output_file)

    discovered = []
    for path in input_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in candidate_exts:
            discovered.append(path)

    # Write JSONL output (one JSON object per line). JSONL is nice for streaming and
    # incremental processing; each line is a complete JSON object.
    with output_file.open("w", encoding="utf-8") as f:
        for email_path in discovered:
            record = {
                "source_path": str(email_path),
                # Fields below are placeholders to be populated by real parsers later.
                "vessel": None,
                "voyage": None,
                "eta": None,
                "terminal": None,
                "subject": None,
                "parsed": False,  # Signals this is a stub record for now
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Discovered {len(discovered)} exported email files.")
    print(f"Wrote JSONL to: {output_file}")
    return 0


def generate_checklist_command(input_jsonl: Path, output_dir: Path) -> int:
    """
    Generate markdown checklists from parsed email data.

    Parameters
    - input_jsonl: Path to JSONL file produced by `parse-emails`.
    - output_dir: Directory to write markdown checklist files.

    Behavior (initial stub):
    - Read each JSON record and create a simple checklist file with placeholders.
    - File is named using the email filename stem where possible; otherwise a counter.
    - This gives a visible output you can review while we develop real templates.
    """
    ensure_directory_exists(output_dir)

    if not input_jsonl.exists():
        print(f"Input not found: {input_jsonl}", file=sys.stderr)
        return 1

    created = 0
    with input_jsonl.open("r", encoding="utf-8") as f:
        for index, line in enumerate(f, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON on line {index}", file=sys.stderr)
                continue

            # Determine filename stem from source path if available
            stem = Path(record.get("source_path", f"email_{index}")).stem
            outfile = output_dir / f"{stem}_checklist.md"

            # Minimal, generic checklist. We will later inject real templates.
            content = (
                f"# Pre-stow Checklist for {record.get('vessel') or 'UNKNOWN VESSEL'}\n\n"
                "- [ ] Confirm ETA and terminal\n"
                "- [ ] Verify voyage and berth plan\n"
                "- [ ] Validate required documentation received\n"
                "- [ ] Note exceptions and follow-ups\n"
            )

            with outfile.open("w", encoding="utf-8") as outf:
                outf.write(content)

            created += 1

    print(f"Generated {created} checklist file(s) in: {output_dir}")
    return 0


def validate_invoices_command(input_path: Path, output_report: Path) -> int:
    """
    Validate invoice CSV/Excel data and emit a human-readable markdown report.

    Parameters
    - input_path: Path to CSV/Excel file containing invoice data to validate.
    - output_report: Markdown report path listing errors/warnings per row.

    Behavior (initial stub):
    - We do not yet know the actual schema. This function will only check that
      the file exists and write a placeholder report describing next steps.
    - Once you provide column names and rules, we will implement real validation.
    """
    ensure_directory_exists(output_report)

    if not input_path.exists():
        print(f"Invoice file not found: {input_path}", file=sys.stderr)
        return 1

    # Write a placeholder report
    report_lines = [
        f"# Invoice Validation Report\n",
        f"Input file: `{input_path}`\n\n",
        "This is a placeholder report. Provide schema (required columns and rules) ",
        "to implement real validations (e.g., missing fields, date formats, numeric ",
        "ranges, cross-field consistency).\n",
    ]

    output_report.write_text("".join(report_lines), encoding="utf-8")
    print(f"Wrote placeholder validation report to: {output_report}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """
    Build the top-level argument parser with subcommands.

    Why a subcommand structure?
    - Each operation (parse emails, generate checklists, validate invoices) has
      distinct inputs/outputs and options. Subcommands keep the UX clear and
      make future extensions straightforward.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Outlook + Invoice Workflow Helper: safe, read-only utilities to support "
            "maritime operations (Outlook parsing, checklist generation, invoice QA)."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # parse-emails
    p_parse = subparsers.add_parser(
        "parse-emails",
        help="Parse exported Outlook emails and emit JSONL records (read-only)",
    )
    p_parse.add_argument(
        "--in",
        dest="input_dir",
        type=Path,
        required=True,
        help="Directory containing exported emails (.eml/.msg/.txt)",
    )
    p_parse.add_argument(
        "--out",
        dest="output_file",
        type=Path,
        required=True,
        help="Output JSONL file path",
    )

    # gen-checklist
    p_check = subparsers.add_parser(
        "gen-checklist",
        help="Generate markdown checklists from parsed email JSONL",
    )
    p_check.add_argument("--in", dest="input_jsonl", type=Path, required=True)
    p_check.add_argument("--out", dest="output_dir", type=Path, required=True)

    # validate-invoices
    p_valid = subparsers.add_parser(
        "validate-invoices",
        help="Validate invoices (CSV/Excel) and emit a markdown report (placeholder)",
    )
    p_valid.add_argument("--in", dest="input_path", type=Path, required=True)
    p_valid.add_argument("--out", dest="output_report", type=Path, required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    """
    Program entry point. Parses CLI args and dispatches to the right subcommand.
    Returns integer exit code (0 = success, non-zero = error).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "parse-emails":
        return parse_emails_command(args.input_dir, args.output_file)
    if args.command == "gen-checklist":
        return generate_checklist_command(args.input_jsonl, args.output_dir)
    if args.command == "validate-invoices":
        return validate_invoices_command(args.input_path, args.output_report)

    # argparse ensures we never get here (required=True for subcommands), but
    # keeping a defensive return is a good practice.
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())


