CREATE VIEW vw_risk_analysis AS
SELECT
    risk_category,
    alert,
    COUNT(*) AS transaction_count,
    ROUND(
        COUNT(*) * 100.0
        / (SELECT COUNT(*) FROM fraud_risk_scores),
    2)
    AS percentage_distribution,
    COUNT(CASE WHEN actual_fraud = 1 THEN 1 END) AS actual_fraud_transactions
FROM fraud_risk_scores
GROUP BY risk_category, alert;

SELECT *
FROM vw_risk_analysis
ORDER BY transaction_count DESC;