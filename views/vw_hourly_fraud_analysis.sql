CREATE VIEW vw_hourly_fraud_analysis AS
SELECT
    HOUR(
        STR_TO_DATE(
            trans_date_trans_time,
            '%Y-%m-%d %H:%i:%s'
        )
    ) AS transaction_hour,
    COUNT(*) AS fraud_transactions
FROM transactions_master
WHERE is_fraud = 1
GROUP BY transaction_hour;

SELECT *
FROM vw_hourly_fraud_analysis
ORDER BY fraud_transactions DESC;