# RA Operations Control Tower

## Problem

Operational trackers often contain the information needed for management reporting, but turning them into a repeatable KPI, RAG, overdue and RAID view can depend on manual spreadsheet work.

## Solution

RA Operations Control Tower v0.1 is a deterministic Python CLI that reads a CSV or Microsoft Excel XLSX tracker, validates the input contract, calculates operational KPIs, assigns project-level RAG status, extracts overdue and RAID records, and writes a five-sheet Excel report.

The five output sheets are: KPIs, RAG, Overdue, RAID, and Executive_Summary.

## Verified evidence

- 10 / 10 approved unit tests passing
- CSV end-to-end smoke passing
- XLSX end-to-end smoke passing
- generated reports opened successfully in Microsoft Excel
- five-sheet output contract verified
- no third-party Python runtime dependencies
- RA Verifier Agent PASS on the approved artifact

## Safety and scope

v0.1 is a local reporting tool. It does not call an LLM, external API, notification service or web application. Input validation is fail-fast, and missing presentation values are rendered as N/A rather than invented.

## Business value

The project demonstrates a reproducible way to turn task-level operational data into management-ready reporting while keeping calculation rules inspectable.

## Public proof

Repository: https://github.com/rash1ed/ra-operations-control-tower

Validation: https://github.com/rash1ed/ra-operations-control-tower/blob/main/docs/validation.txt

CI: https://github.com/rash1ed/ra-operations-control-tower/actions

Excel evidence: https://github.com/rash1ed/ra-operations-control-tower/tree/main/docs/evidence
