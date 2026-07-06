SELECT
    ROUND(AVG(risk_score), 2) AS average_risk_score
FROM fraud_risk_scores;

SELECT
	risk_category,
    COUNT(*) AS transaction_count
FROM fraud_risk_scores
GROUP BY risk_category
ORDER BY transaction_count DESC;

SELECT
    risk_category,
    COUNT(*) AS transaction_count,
    ROUND(
        COUNT(*) * 100.0
        / (SELECT COUNT(*) FROM fraud_risk_scores),
    2) 
    AS percentage_distribution
FROM fraud_risk_scores
GROUP BY risk_category
ORDER BY percentage_distribution DESC;

SELECT
    alert,
    COUNT(*) AS alert_count
FROM fraud_risk_scores
GROUP BY alert
ORDER BY alert_count DESC;

SELECT
    risk_category,
    COUNT(*) AS actual_fraud_transactions
FROM fraud_risk_scores
WHERE actual_fraud = 1
GROUP BY risk_category
ORDER BY actual_fraud_transactions DESC;