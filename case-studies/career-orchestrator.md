# RA Career Orchestrator

## Problem

A career automation stack can have multiple independent execution lanes. A scheduler may be healthy while a portal lane is blocked, or a local worker may be fresh while cloud health is unavailable. Treating the whole system as simply "up" or "down" hides those differences.

## Solution

RA Career Orchestrator v0.1 is a deterministic, read-only coordination and health-reconciliation control plane.

It observes RA AI OS V1 Local Worker, RA Action Bridge V5, BrowserExecutorV2 / Portal Bridge, optional cloud-health evidence, and configured Windows Scheduled Tasks. It reconciles lane states into PASS, DEGRADED or HOLD and writes JSON, Markdown and NDJSON evidence.

## Verified evidence

- 12 / 12 approved unit tests passing
- independent contract audit PASS
- autonomous Windows scheduled execution every five minutes
- scheduled-task Last Result = 0 in the recorded validation
- live read-only smoke completed

The live smoke is deliberately reported as DEGRADED rather than falsely green: local AI and Action Bridge are PASS, the Portal lane contains human/safe-next outcomes, and the Cloud lane is EXTERNAL until a read-only cloud-health export is connected.

## Safety and scope

v0.1 has no authority to send email, submit job applications, automate LinkedIn, modify CVs, mutate production queues, or replace sender/router logic.

## Business value

The project demonstrates evidence-first operational monitoring: each lane is reported independently, and the worst meaningful state is surfaced instead of hiding a partial failure behind a successful scheduler heartbeat.

## Public proof

Repository: https://github.com/rash1ed/ra-career-orchestrator

Validation: https://github.com/rash1ed/ra-career-orchestrator/blob/main/docs/validation.txt

Live smoke: https://github.com/rash1ed/ra-career-orchestrator/blob/main/docs/live-smoke-sanitized.json

CI: https://github.com/rash1ed/ra-career-orchestrator/actions
