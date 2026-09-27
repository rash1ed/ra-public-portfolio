SELECT
    channel,
    priority,
    COUNT(*) AS tickets,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS portfolio_pct
FROM tickets
GROUP BY channel, priority
ORDER BY channel, CASE priority WHEN 'Critical' THEN 1 WHEN 'High' THEN 2 WHEN 'Medium' THEN 3 ELSE 4 END;
