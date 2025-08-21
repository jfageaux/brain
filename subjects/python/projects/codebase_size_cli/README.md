# Codebase Size CLI

A beginner-friendly Python command-line tool to measure how much disk space your codebase uses.

## Run (Windows PowerShell)
```powershell
python subjects\python\projects\codebase_size_cli\codebase_size.py
python subjects\python\projects\codebase_size_cli\codebase_size.py --by-ext --top 10
python subjects\python\projects\codebase_size_cli\codebase_size.py --json
```

## Options
- --path PATH: directory to scan (default: current directory)
- --include-hidden: include dot files/folders
- --follow-symlinks: follow symlinks
- --no-default-excludes: do not exclude common cache/dependency dirs
- --exclude <names...>: extra directory names to exclude
- --by-ext: show extension breakdown
- --top N: show N largest files
- --json: output JSON

## Notes
- Uses only Python standard library, no extra installs needed.
- Excludes common noise (e.g., `.git`, `__pycache__`, `node_modules`, `venv`) by default.
