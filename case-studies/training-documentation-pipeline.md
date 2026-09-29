# Training & Documentation Pipeline

## Problem

Training and SOP work can become difficult to manage when ownership, audience, required steps, and review requirements are scattered across documents and messages.

## Solution

Training & Documentation Pipeline is a deterministic Python example that validates module inputs, normalizes documented steps, applies review gates to external or policy-sensitive material, and summarizes plan-level readiness.

## Verified evidence

- 10 / 10 unit tests passing
- Explicit `READY`, `WAITING_REVIEW`, and `HOLD` states
- Required metadata and step validation
- Review gates for external or policy-sensitive material
- Synthetic examples only

## Business value

The project demonstrates documentation governance, training coordination, requirements checking, review workflows, and management reporting relevant to Operations, PMO, and Business Analysis roles.

## Public proof

See `training-documentation-pipeline/README.md` and `training-documentation-pipeline/docs/validation.txt` in this portfolio repository.
