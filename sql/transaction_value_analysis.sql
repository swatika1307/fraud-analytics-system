SELECT
	ROUND(SUM(amt), 2) AS total_transaction_value
FROM transactions_master;

SELECT
	ROUND(SUM(amt), 2) AS total_fraud_value
FROM transactions_master
WHERE is_fraud = 1;

SELECT
	ROUND(
		(
			SUM(CASE WHEN is_fraud = 1 THEN amt ELSE 0 END)
            * 100.0
		) / SUM(amt),
	4)
    AS fraud_value_percentage
FROM transactions_master;