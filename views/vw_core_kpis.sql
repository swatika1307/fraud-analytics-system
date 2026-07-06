CREATE VIEW vw_core_kpis AS
SELECT
    COUNT(*) AS total_transactions,
    COUNT(CASE WHEN is_fraud = 1 THEN 1 END) AS total_fraud_transactions,
    ROUND(
        COUNT(CASE WHEN is_fraud = 1 THEN 1 END)
        * 100.0 / COUNT(*),
    4)
    AS fraud_rate_percentage,
    ROUND(SUM(amt), 2) AS total_transaction_value,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN amt ELSE 0 END),
	2)
    AS total_fraud_value,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN amt ELSE 0 END)
        * 100.0 / SUM(amt),
	4)
    AS fraud_value_percentage
FROM transactions_master;

SELECT *
FROM vw_core_kpis;