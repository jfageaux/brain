# Maritime Operations (Port Captain & Agency) 🚢

Welcome to your domain-specific hub for maritime and port operations. This subject captures workflows and tools relevant to your roles at COSCO Shipping Long Beach:

- Port Captain / Owners Agent (vessel planning)
- Boarding Agent (customs broker liaison)
- Marine Operations Pre-stow Coordinator
- Outlook-heavy communications and COSCO invoice data entry systems

## 🎯 Focus

- Transform recurring operational tasks into documented, automatable workflows
- Build small tools to assist Outlook triage, document preparation, and invoice QA
- Create SOPs and checklists that are versioned and continuously improved
- Integrate with Python projects to automate parts of your daily routine

## 📁 Structure

- `notes/`: SOPs, checklists, templates, process maps
- `exercises/`: Practice tasks turning SOPs into semi-automation
- `projects/`: Real tools that support your work (e.g., Outlook helpers, invoice validators)

## 🧭 Learning Pathway (Practical)

1) Document the workflows
   - Outlook triage: inbox rules, follow-up flags, templates
   - Vessel call lifecycle: pre-arrival → arrival → operations → departure → post-call
   - Customs/boarding documentation: forms, timelines, stakeholders
   - Invoice data entry: required fields, sources, common errors, QA steps

2) Prototype helpers (no-risk, read-only first)
   - Email subject/body parsers to extract ETA, vessel/voyage, terminal, berth, cutoffs
   - Template generators for standard replies and pre-stow checklists
   - CSV/Excel validators for required invoice fields

3) Automate safely
   - Batch rename/download attachments to structured folders
   - Generate pre-filled forms/checklists from parsed emails
   - Produce daily summaries (planned vs actual ETAs, outstanding docs, exceptions)

## 🤝 Cross-Subject Integration

- Python: automation scripts, parsers, validators
- Git: versioned SOPs, change history, incident post-mortems
- AI: draft emails, summarize long threads, anomaly detection in invoices
- Philosophy/Ethics: decision logs for exceptions, fairness and compliance
- Psychology: cognitive load reduction with templates and checklists

## 🛠️ Starter Projects

1) Outlook Triage Assistant (read-only)
   - Parse saved `.eml`/`.msg` or exported `.txt` emails from Outlook
   - Extract key fields (vessel, voyage, ETA, terminal) with regex rules
   - Output a structured JSON/CSV for planning

2) Invoice Field Validator
   - Define required fields schema (vessel, voyage, dates, amounts)
   - Validate CSV/Excel exports before COSCO system entry
   - Produce a human-readable QA report

3) Pre-stow Checklist Generator
   - Simple CLI that asks questions and outputs a standardized checklist
   - Saves timestamped files for audit trail

## ✅ Outcomes

- Clear SOPs and templates ready to use daily
- Small utilities that remove repetitive steps
- Documented improvements feeding back into your learning roadmap

---

Start in `notes/getting_started.md` to capture your current workflow with checklists and templates.


