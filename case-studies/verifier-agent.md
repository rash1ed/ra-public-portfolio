# RA Verifier Agent v0.1 — Evidence-First Artifact Verification

## Business problem

A project can look complete while its evidence is missing, stale or inconsistent with the claims made about it.

## System

RA Verifier Agent checks a project artifact against explicit JSON criteria and returns PASS, FAIL or HOLD.

v0.1 checks:
1. Required files.
2. Expected SHA-256 values when configured.
3. A configured test command and its exit code.
4. Simple secret patterns in text files.
5. Numeric claims against declared evidence using explicit regex rules.

## Verified proof

- **8 / 8 verifier tests passing**
- Excel Assurance Engine verification result: **PASS**
- GitHub Actions CI: **success**
- Test commands execute against a temporary copy instead of the source artifact
- Public repository: https://github.com/rash1ed/ra-verifier-agent

## Safety design

The verifier does not repair the artifact. It reports evidence and status only. A concrete failed check produces FAIL; an incomplete check that cannot run produces HOLD.

## What this demonstrates

- evidence-first delivery
- independent verification logic
- test orchestration
- non-mutating validation
- secret scanning
- claim-to-evidence controls
- reproducible CI
