WITH open_tickets AS (
    SELECT
        t.*,
        CAST(julianday('2026-09-27 12:00:00') - julianday(opened_at) AS INTEGER) AS age_days
    FROM tickets t
    WHERE status <> 'Resolved'
)
SELECT
    CASE
        WHEN age_days <= 1 THEN '0-1 days'
        WHEN age_days <= 3 THEN '2-3 days'
        WHEN age_days <= 7 THEN '4-7 days'
        ELSE '8+ days'
    END AS age_bucket,
    COUNT(*) AS ticket_count,
    SUM(priority IN ('High','Critical')) AS high_priority_count
FROM open_tickets
GROUP BY age_bucket
ORDER BY MIN(age_days);
