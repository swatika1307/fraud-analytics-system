SELECT
    ROUND(AVG(amt), 2) AS average_fraud_transaction_amount
FROM transactions_master
WHERE is_fraud = 1;

SELECT
    ROUND(MAX(amt), 2) AS highest_fraud_transaction_amount
FROM transactions_master
WHERE is_fraud = 1;

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
GROUP BY transaction_hour
ORDER BY fraud_transactions DESC;

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
GROUP BY transaction_day
ORDER BY fraud_transactions DESC;

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
GROUP BY transaction_month
ORDER BY fraud_transactions DESC;