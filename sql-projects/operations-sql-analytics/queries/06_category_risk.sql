SELECT
    category,
    COUNT(*) AS tickets,
    SUM(status <> 'Resolved') AS backlog,
    SUM(priority = 'Critical' AND status <> 'Resolved') AS critical_open,
    ROUND(100.0 * SUM(status <> 'Resolved') / COUNT(*), 1) AS backlog_pct
FROM tickets
GROUP BY category
ORDER BY critical_open DESC, backlog_pct DESC, category;
