# Excel Assurance Engine v0.1 — Workbook QA for Operational Reporting

## Business problem

Operational spreadsheets can look finished while still containing risks such as duplicate rows, blank required fields, stored error values, hidden sheets or formulas pointing to missing sheets.

## System

The Excel Assurance Engine reads .xlsx files directly as OOXML packages and applies five deterministic checks:

1. Stored Excel error values.
2. Exact duplicate data rows.
3. Blank values in configured required columns.
4. Hidden or very-hidden worksheets.
5. Formula references to worksheet names that do not exist.

## Verified proof

- **5 / 5 automated tests passing**
- **3 reproducible sample workbooks**
- Issue-rich workbook: **6 findings across all five categories**
- Clean workbook: **0 findings**
- Quoted-sheet-reference workbook: **1 expected required-column finding**
- **0 third-party Python runtime dependencies**
Public repository: https://github.com/rash1ed/ra-excel-assurance-engine

## Safety design

v0.1 does not silently repair business data.

The generated corrected.xlsx is intentionally a byte-identical review copy. Duplicate removal, formula rewrites, filling missing values and unhiding sheets require business context and explicit review.

## What this demonstrates

- Excel and workbook structure understanding
- Data-quality controls
- Operations reporting QA
- Deterministic testing
- Evidence-first delivery
- Non-destructive automation
- Technical-to-business translation
