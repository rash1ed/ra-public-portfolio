# RA Career Action Engine

## Problem

Career workflows can mix opportunity detection, matching, drafting and application state in a way that makes it hard to distinguish preparation from an actual external submission.

## Solution

RA Career Action Engine v0.1 is a deterministic local Python pipeline that proves a controlled opportunity workflow using synthetic labelled email fixtures.

It parses supported fixture patterns, builds deterministic canonical identities for deduplication, computes an integer-only profile match score, classifies results, renders source-locked drafts for eligible matches, and writes tracker and summary evidence locally.

## Verified evidence

- 13 / 13 approved unit tests passing
- independent contract audit PASS
- CLI smoke PASS
- four synthetic messages processed in the smoke run
- every tracker record remained `submission_state = NOT_SENT`
- no third-party Python runtime dependencies

## Safety and scope

v0.1 intentionally has no Gmail API, SMTP sending, LinkedIn session automation, scraping, browser automation, LLM calls or scheduler.

Its public fixtures are synthetic. The draft renderer is source-locked and cannot invent skills, qualifications or experience from job-body text.

## Business value

The project demonstrates auditable separation between detection, matching, drafting and actual submission state, reducing the risk of falsely reporting an application as sent.

## Public proof

Repository: https://github.com/rash1ed/ra-career-action-engine

Validation: https://github.com/rash1ed/ra-career-action-engine/blob/main/docs/validation.txt

CI: https://github.com/rash1ed/ra-career-action-engine/actions
