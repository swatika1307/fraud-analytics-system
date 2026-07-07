CREATE VIEW vw_daily_fraud_analysis AS
SELECT
    DAYNAME(
        STR_TO_DATE(
            trans_date_trans_time,
            '%Y-%m-%d %H:%i:%s'
        )
    ) AS transaction_day,
    COUNT(*) AS fraud_transactions
FROM transactions_master
WHERE is_fraud = 1
GROUP BY transaction_day;

SELECT *
FROM vw_daily_fraud_analysis
ORDER BY fraud_transactions DESC;