SELECT
transaction_type,
SUM(amount) AS total_amount
FROM bank_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;
