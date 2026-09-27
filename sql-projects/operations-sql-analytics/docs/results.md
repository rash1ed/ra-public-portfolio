# RA Operations SQL Analytics — Verified Demo Results

Synthetic data only. SQLite standard library execution.

## 01_executive_kpis

| total_tickets | resolved_tickets | open_backlog | sla_met_pct | avg_resolution_hours | avg_csat |
|---|---|---|---|---|---|
| 72 | 60 | 12 | 80.0 | 16.2 | 4.2 |

## 02_team_performance

| team_name | tickets | resolved | backlog | sla_met_pct | avg_resolution_hours | avg_csat |
|---|---|---|---|---|---|---|
| West Ops | 24 | 12 | 12 | 100.0 | 19.0 | 4.25 |
| Central Ops | 24 | 24 | 0 | 75.0 | 15.5 | 4.13 |
| North Ops | 24 | 24 | 0 | 75.0 | 15.5 | 4.25 |

## 03_backlog_aging

| age_bucket | ticket_count | high_priority_count |
|---|---|---|
| 4-7 days | 2 | 1 |
| 8+ days | 10 | 5 |

## 04_channel_priority_mix

| channel | priority | tickets | portfolio_pct |
|---|---|---|---|
| Chat | High | 18 | 25.0 |
| Email | Low | 18 | 25.0 |
| Phone | Medium | 18 | 25.0 |
| Web | Critical | 18 | 25.0 |

## 05_agent_rankings

| agent_code | team_name | tickets | resolved | backlog | sla_met_pct | avg_csat | performance_rank |
|---|---|---|---|---|---|---|---|
| Agent A | North Ops | 12 | 12 | 0 | 100.0 | 4.25 | 1 |
| Agent E | West Ops | 12 | 12 | 0 | 100.0 | 4.25 | 1 |
| Agent C | Central Ops | 12 | 12 | 0 | 100.0 | 4.17 | 2 |
| Agent B | North Ops | 12 | 12 | 0 | 50.0 | 4.25 | 3 |
| Agent D | Central Ops | 12 | 12 | 0 | 50.0 | 4.08 | 4 |
| Agent F | West Ops | 12 | 0 | 12 |  |  | 5 |

## 06_category_risk

| category | tickets | backlog | critical_open | backlog_pct |
|---|---|---|---|---|
| Technical | 15 | 3 | 2 | 20.0 |
| Billing | 15 | 3 | 1 | 20.0 |
| Account | 14 | 2 | 1 | 14.3 |
| Delivery | 14 | 2 | 1 | 14.3 |
| General | 14 | 2 | 1 | 14.3 |

