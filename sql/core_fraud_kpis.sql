SELECT COUNT(*) AS total_transactions FROM transactions_master;

SELECT COUNT(*) AS total_fraud_transactions 
FROM transactions_master
WHERE is_fraud = 1;

SELECT 
	ROUND(
		(COUNT(CASE WHEN is_fraud = 1 THEN 1 END) * 100.0)
        / COUNT(*),
	4)
    AS fraud_rate_percentage
FROM transactions_master;