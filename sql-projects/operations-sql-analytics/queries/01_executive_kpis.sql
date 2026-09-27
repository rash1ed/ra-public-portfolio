WITH resolved AS (
    SELECT *,
           (julianday(resolved_at) - julianday(opened_at)) * 24.0 AS resolution_hours,
           CASE WHEN resolved_at <= due_at THEN 1 ELSE 0 END AS sla_met
    FROM tickets
    WHERE status = 'Resolved'
)
SELECT
    (SELECT COUNT(*) FROM tickets) AS total_tickets,
    (SELECT COUNT(*) FROM resolved) AS resolved_tickets,
    (SELECT COUNT(*) FROM tickets WHERE status <> 'Resolved') AS open_backlog,
    ROUND(100.0 * (SELECT SUM(sla_met) FROM resolved) / NULLIF((SELECT COUNT(*) FROM resolved),0), 1) AS sla_met_pct,
    ROUND((SELECT AVG(resolution_hours) FROM resolved), 1) AS avg_resolution_hours,
    ROUND((SELECT AVG(csat) FROM resolved WHERE csat IS NOT NULL), 2) AS avg_csat;
