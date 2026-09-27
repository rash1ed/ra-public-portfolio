# RA Operations SQL Analytics

A recruiter-facing SQL portfolio project for **Operations, Reporting and Data Analysis** using a fully synthetic service-operations dataset.

The project demonstrates practical SQL rather than isolated syntax exercises. It models teams, agents and service tickets, then answers management questions around SLA performance, backlog, aging, channel mix, team performance and risk.

## What it demonstrates

- relational schema design and foreign keys;
- joins and grouped KPIs;
- CTEs;
- CASE-based business rules;
- window functions (`DENSE_RANK`, window totals);
- SLA and backlog calculations;
- deterministic validation with Python `sqlite3`;
- public-safe synthetic data.

## Business questions

1. What is the overall backlog and SLA attainment?
2. Which teams perform best on SLA, response time and CSAT?
3. How old is the unresolved backlog?
4. Which channel/priority combinations dominate volume?
5. Which agents rank highest on service outcomes?
6. Which categories carry the most operational risk?

## Project structure

- `schema.sql` — normalized SQLite schema.
- `seed.sql` — 72 synthetic tickets, 6 generic agents, 3 teams.
- `queries/01_executive_kpis.sql` — executive KPI summary.
- `queries/02_team_performance.sql` — team SLA/backlog/CSAT view.
- `queries/03_backlog_aging.sql` — backlog aging buckets.
- `queries/04_channel_priority_mix.sql` — window-function portfolio mix.
- `queries/05_agent_rankings.sql` — ranking with `DENSE_RANK`.
- `queries/06_category_risk.sql` — category backlog and critical-open risk.
- `tests/test_sql_analytics.py` — deterministic validation.
- `docs/results.md` — verified query outputs.

## Run

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python run_demo.py
```

Runtime uses only Python's standard-library `sqlite3` module.

## Public-data boundary

All names, tickets, dates and metrics are synthetic. Agents use generic identifiers (`Agent A` ... `Agent F`). No employer, customer, credential, email, phone number or private operational data is included.
