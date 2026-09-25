# RA | Operations, PMO, Data & Automation Portfolio

**RASHID ABDULAZIZ — Saudi Arabia**

This portfolio focuses on practical operations, PMO, reporting and automation work with evidence that can be inspected and reproduced.

## Core areas

- Operations and process improvement
- PMO support, governance and reporting
- Excel and business data quality
- Power BI and management reporting
- Workflow automation with verification and recovery controls

## Verified proof

### Excel Assurance Engine v0.1

A dependency-light QA engine for .xlsx workbooks used in operations, PMO and reporting.

Verified results from the public project:
- **5 / 5 automated tests passing**
- **5 deterministic QA checks**
- **3 reproducible sample workbooks**
- Issue-rich sample: **6 findings across all five audit categories**
- Clean sample: **0 findings**
- Quoted-sheet-reference sample: **1 expected required-column finding**
- Runtime dependencies: **0 third-party Python packages**

Public repository: https://github.com/rash1ed/ra-excel-assurance-engine

Direct evidence:
- Validation: https://github.com/rash1ed/ra-excel-assurance-engine/blob/main/docs/validation.txt
- Tests: https://github.com/rash1ed/ra-excel-assurance-engine/tree/main/tests
- CI: https://github.com/rash1ed/ra-excel-assurance-engine/actions

### RA Verifier Agent v0.1

An evidence-first verifier that checks required files, SHA-256 expectations, configured tests, secret patterns and numeric claims against evidence.

Verified public results:
- **8 / 8 verifier tests passing**
- Excel Assurance Engine verification: **PASS**
- PASS / FAIL / HOLD status model
- Configured tests execute against a temporary copy instead of mutating the source artifact
- GitHub Actions CI: **success**

Public repository: https://github.com/rash1ed/ra-verifier-agent

Direct evidence:
- Validation: https://github.com/rash1ed/ra-verifier-agent/blob/main/docs/validation.txt
- Excel verification: https://github.com/rash1ed/ra-verifier-agent/blob/main/docs/excel-engine-verification.txt
- Tests: https://github.com/rash1ed/ra-verifier-agent/tree/main/tests
- CI: https://github.com/rash1ed/ra-verifier-agent/actions

### RA Operations Control Tower v0.1

A deterministic operations-reporting CLI for validated CSV/XLSX trackers.

Verified public results:
- **10 / 10 approved tests passing**
- CSV and Microsoft Excel XLSX end-to-end smoke passing
- five-sheet Excel reporting contract
- generated reports opened successfully in Microsoft Excel
- runtime dependencies: **0 third-party Python packages**

Public repository: https://github.com/rash1ed/ra-operations-control-tower

### RA Career Action Engine v0.1

A deterministic, local proof of a controlled opportunity workflow with explicit NOT_SENT state.

Verified public results:
- **13 / 13 approved tests passing**
- contract audit: **PASS**
- CLI smoke: **PASS**
- public fixtures are synthetic
- no sending, scraping, LinkedIn session automation, browser automation or LLM calls

Public repository: https://github.com/rash1ed/ra-career-action-engine

### RA Career Orchestrator v0.1

A read-only health-reconciliation control plane for the existing Career OS.

Verified public results:
- **12 / 12 approved tests passing**
- contract audit: **PASS**
- autonomous Windows run every five minutes
- recorded scheduler Last Result: **0**
- live smoke reports lane-level truth rather than forcing a false green state

Public repository: https://github.com/rash1ed/ra-career-orchestrator

## Featured case studies

### 01 — Excel Assurance Engine
Workbook QA for operational reporting with direct OOXML parsing, evidence reports and non-destructive review copies.

[Read the case study](case-studies/excel-assurance-engine.md)

### 02 — RA Verifier Agent
Independent verification of project artifacts with PASS / FAIL / HOLD controls, test re-execution, secret scanning and claim-to-evidence checks.

[Read the case study](case-studies/verifier-agent.md)

### 03 — Career Operations OS
An auditable career workflow covering discovery, verification, routing, follow-up and execution evidence.

[Read the case study](case-studies/career-operations-os.md)

### 04 — Client Delivery Automation
A structured project-delivery workflow covering inputs, revisions, schedules, BOQs, QA, packaging and recovery.

[Read the case study](case-studies/client-delivery-automation.md)

### 05 — RA Operations Control Tower
Deterministic operations reporting from validated CSV/XLSX trackers into KPI, RAG, overdue, RAID and executive-summary views.

[Read the case study](case-studies/operations-control-tower.md)

### 06 — RA Career Action Engine
A controlled local opportunity pipeline that keeps preparation evidence separate from external submission state.

[Read the case study](case-studies/career-action-engine.md)

### 07 — RA Career Orchestrator
Read-only health reconciliation across local worker, action bridge, portal and cloud-evidence lanes.

[Read the case study](case-studies/career-orchestrator.md)
## What I bring to an operations or PMO team

1. Define a reliable source of truth.
2. Break work into measurable stages.
3. Automate repeatable checks where results can be verified.
4. Build reporting around the real workflow.
5. Preserve human accountability for sensitive decisions.
6. Improve processes from observed failure modes.

## Recruiter view

- [Recruiter One-Pager](docs/recruiter-one-pager.md)
- [Public Proof Register](docs/proof-register.md)
- [Proof Engine](docs/proof-engine.md)

A browser-ready landing page is available in [index.html](index.html).

## Public-safe by design

This repository excludes credentials, private endpoints, employer correspondence, personal application records and unverified numeric claims.
