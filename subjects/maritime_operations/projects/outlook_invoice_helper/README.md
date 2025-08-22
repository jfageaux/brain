# Outlook + Invoice Workflow Helper

A practical, comment-driven project to support your daily maritime operations. Start read-only and iterate safely.

## Goals

- Parse exported Outlook emails to extract vessel/voyage/ETA/terminal
- Generate standardized checklists and pre-filled templates
- Validate invoice CSV/Excel data before entry into COSCO system

## Safety First

- Read-only parsing at first (no email sending, no system writes)
- Work on exported files (.eml/.msg/.txt, CSV/Excel) in a sandbox folder
- Produce clear, auditable outputs (JSON, CSV, Markdown reports)

## Milestones

1) Email Parser (read-only)
   - Input: exported emails
   - Output: JSON lines with extracted fields
2) Checklist Generator
   - Input: parsed JSON
   - Output: Markdown checklist with timestamps
3) Invoice Validator
   - Input: CSV/Excel export
   - Output: Validation report with errors/warnings and line references

## Suggested Tech

- Python standard library (pathlib, csv, json, re, argparse)
- Optional: `pandas` for Excel/CSV convenience
- Follow `subjects/python/notes/project_template.py` for heavy comments

## Usage (planned)

```powershell
python main.py parse-emails --in exports/emails --out data/parsed.jsonl
python main.py gen-checklist --in data/parsed.jsonl --out out/checklists/
python main.py validate-invoices --in data/invoices.csv --out out/validation.md
```

## Notes

- Keep comments extensive to match the codebase standard
- Log assumptions and edge cases you encounter in real work
- Grow features incrementally based on your workflow pain points


