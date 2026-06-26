SELECT
	category,
    COUNT(*) AS fraud_transactions
FROM transactions_master
WHERE is_fraud = 1
GROUP BY category
ORDER BY fraud_transactions DESC;

SELECT
	category,
    ROUND(SUM(amt), 2) AS total_fraud_value
FROM transactions_master
WHERE is_fraud = 1
GROUP BY category
ORDER BY total_fraud_value DESC;

SELECT
	category,
	COUNT(CASE WHEN is_fraud = 1 THEN 1 END) AS fraud_transactions,
    COUNT(*) AS total_transactions,
    ROUND(
		COUNT(CASE WHEN is_fraud = 1 THEN 1 END) * 100.0
        / COUNT(*),
	2)
    AS fraud_rate_percentage
FROM transactions_master
GROUP BY category
ORDER BY fraud_rate_percentage DESC;