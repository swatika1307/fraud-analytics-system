CREATE VIEW vw_geographic_analysis AS
SELECT
    state,
    COUNT(*) AS total_transactions,
    COUNT(CASE WHEN is_fraud = 1 THEN 1 END) AS fraud_transactions,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN amt ELSE 0 END),
        2
    ) AS total_fraud_value,
    ROUND(
        COUNT(CASE WHEN is_fraud = 1 THEN 1 END)
        * 100.0 / COUNT(*),
    2)
    AS fraud_rate_percentage
FROM transactions_master
GROUP BY state;

SELECT *
FROM vw_geographic_analysis
ORDER BY fraud_transactions DESC;