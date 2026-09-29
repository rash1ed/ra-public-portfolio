# Training & Documentation Pipeline

A deterministic planning project for turning operational knowledge into structured training modules and controlled documentation.

## Business use

The pipeline helps an Operations or PMO team make training work visible: required inputs, owners, audience, documented steps, review gates, and plan-level status counts.

## Controls included

- Required metadata validation
- Step normalization
- Review gates for external or policy-sensitive material
- Explicit `READY`, `WAITING_REVIEW`, and `HOLD` states
- Plan-level counts for management reporting
- Simple completion-rate calculation

## Run validation

```cmd
cd training-documentation-pipeline
python -m unittest discover -s tests -p "test_*.py" -v
```

## Public-data boundary

All examples are synthetic. The project does not contain employer training material, confidential SOPs, customer data, or credentials.

## Files

- `training_pipeline.py` — deterministic planning logic
- `tests/test_training_pipeline.py` — unit tests
- `samples/modules.json` — synthetic example modules
- `docs/validation.txt` — latest validation transcript
