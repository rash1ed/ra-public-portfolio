WITH agent_perf AS (
    SELECT
        a.agent_code,
        tm.team_name,
        COUNT(t.ticket_id) AS tickets,
        SUM(t.status = 'Resolved') AS resolved,
        SUM(t.status <> 'Resolved') AS backlog,
        ROUND(100.0 * SUM(CASE WHEN t.status='Resolved' AND t.resolved_at <= t.due_at THEN 1 ELSE 0 END)
              / NULLIF(SUM(t.status='Resolved'),0), 1) AS sla_met_pct,
        ROUND(AVG(CASE WHEN t.status='Resolved' THEN t.csat END),2) AS avg_csat
    FROM agents a
    JOIN teams tm ON tm.team_id = a.team_id
    LEFT JOIN tickets t ON t.agent_id = a.agent_id
    GROUP BY a.agent_id, a.agent_code, tm.team_name
)
SELECT
    agent_code,
    team_name,
    tickets,
    resolved,
    backlog,
    sla_met_pct,
    avg_csat,
    DENSE_RANK() OVER (ORDER BY sla_met_pct DESC, avg_csat DESC, backlog ASC) AS performance_rank
FROM agent_perf
ORDER BY performance_rank, agent_code;
