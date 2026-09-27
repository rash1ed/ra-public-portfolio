WITH ticket_metrics AS (
    SELECT
        tm.team_name,
        t.status,
        t.csat,
        CASE WHEN t.status = 'Resolved' AND t.resolved_at <= t.due_at THEN 1 ELSE 0 END AS sla_met,
        CASE WHEN t.status = 'Resolved' THEN (julianday(t.resolved_at) - julianday(t.opened_at)) * 24.0 END AS resolution_hours
    FROM tickets t
    JOIN agents a ON a.agent_id = t.agent_id
    JOIN teams tm ON tm.team_id = a.team_id
)
SELECT
    team_name,
    COUNT(*) AS tickets,
    SUM(status = 'Resolved') AS resolved,
    SUM(status <> 'Resolved') AS backlog,
    ROUND(100.0 * SUM(sla_met) / NULLIF(SUM(status = 'Resolved'),0), 1) AS sla_met_pct,
    ROUND(AVG(resolution_hours), 1) AS avg_resolution_hours,
    ROUND(AVG(CASE WHEN status='Resolved' THEN csat END), 2) AS avg_csat
FROM ticket_metrics
GROUP BY team_name
ORDER BY sla_met_pct DESC, backlog ASC, team_name;
