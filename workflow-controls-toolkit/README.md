# Workflow Controls Toolkit

A small, deterministic operations toolkit for validating work items, routing them to queues, splitting actions into trackable tasks, applying approval gates, and defining bounded retry behavior.

## Business use

This project demonstrates practical process-control patterns for Operations, PMO, service delivery, and reporting workflows without relying on hidden model decisions.

## Controls included

- Required-field validation
- Rule-based queue routing
- Task fan-out with stable task IDs
- Approval gates for high-risk or high-value items
- Bounded exponential retry timing
- Explicit `READY`, `WAITING_APPROVAL`, and `HOLD` states

## Run validation

```cmd
cd workflow-controls-toolkit
python -m unittest discover -s tests -p "test_*.py" -v
```

## Public-data boundary

All sample data is synthetic. The toolkit has no email, browser, credential, job-board, or external-system authority.

## Files

- `workflow_toolkit.py` — deterministic workflow functions
- `tests/test_workflow_toolkit.py` — unit tests
- `samples/items.json` — synthetic example inputs
- `docs/validation.txt` — latest validation transcript
