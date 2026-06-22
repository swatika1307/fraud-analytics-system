SELECT
	ROUND(SUM(amt), 2) AS total_transaction_value
FROM transactions_master;

SELECT
	ROUND(SUM(amt), 2) AS total_fraud_value
FROM transactions_master
WHERE is_fraud = 1;