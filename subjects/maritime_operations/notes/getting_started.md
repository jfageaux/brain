# Maritime Ops Getting Started

Use this file to quickly capture your real workflows and turn them into versioned SOPs.

## Roles & Core Workflows

- Port Captain / Owners Agent (vessel planning)
- Boarding Agent (customs broker liaison)
- Marine Operations Pre-stow Coordinator

### Daily Inbox Triage (Outlook)
- Key senders and subjects to prioritize
- Saved searches and categories
- Triage checklist (2-minute rule, follow-ups, flags)
- Standard templates/snippets for common cases

### Vessel Call Lifecycle
1. Pre-arrival: required docs, confirmations, contact list
2. Arrival/Alongside: updates, changes, exception handling
3. Operations: pre-stow coordination, comms cadence, stakeholders
4. Departure/Post-call: reports, invoices, record-keeping

### Invoice Data Entry
- Required fields schema (define in a table)
- Source of truth for each field
- Common error patterns and how to detect them
- Quality gate checklist before submission

## Templates

- Email: Pre-arrival request, operations update, post-call summary
- Checklist: Pre-stow, boarding pack, invoice QA
- File naming convention: `[YYYY-MM-DD]_[VESSEL]_[VOY]_[DOC-TYPE]`

## Backlog of Improvements

- Parse saved emails to extract ETA/vessel/voyage
- Auto-generate pre-stow checklist from email fields
- Validate invoice CSV before entry
- Daily digest of outstanding items

---

Next: create `projects/` tools to support the above. Start read-only, then automate.
