CREATE VIEW vw_monthly_fraud_analysis AS
SELECT
    MONTHNAME(
        STR_TO_DATE(
            trans_date_trans_time,
            '%Y-%m-%d %H:%i:%s'
        )
    ) AS transaction_month,
    COUNT(*) AS fraud_transactions
FROM transactions_master
WHERE is_fraud = 1
GROUP BY transaction_month;

SELECT *
FROM vw_monthly_fraud_analysis
ORDER BY fraud_transactions DESC;