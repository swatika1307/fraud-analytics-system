CREATE DATABASE fraud_analytics_db;

SHOW DATABASES;

USE fraud_analytics_db;

SELECT DATABASE();

SHOW TABLES;

SELECT COUNT(*) as sample_values FROM transactions_master;

SELECT COUNT(*) as sample_values FROM fraud_risk_scores;