-- Calculate the total loan amount during a specific time period
SELECT SUM(total_loan_amount) AS total_loan_amount
FROM transactions
WHERE settlement_date BETWEEN '2023-01-01' AND '2023-03-31';

-- Calculate the highest loan amount given by a broker
SELECT broker, MAX(total_loan_amount) AS highest_loan_amount
FROM transactions
GROUP BY broker
ORDER BY highest_loan_amount DESC
LIMIT 1;

-- Generate a report for the broker, sorting loan amounts in descending order
SELECT settlement_date, broker, total_loan_amount
FROM transactions
ORDER BY total_loan_amount DESC;

-- Generate a report of the total loan amount grouped by date
SELECT settlement_date, SUM(total_loan_amount) AS total_loan_amount
FROM transactions
GROUP BY settlement_date
ORDER BY settlement_date;

-- Define tier level of each transaction
SELECT
    settlement_date,
    broker,
    total_loan_amount,
    CASE
        WHEN total_loan_amount > 100000 THEN 'Tier 1'
        WHEN total_loan_amount > 50000 THEN 'Tier 2'
        WHEN total_loan_amount > 10000 THEN 'Tier 3'
        ELSE 'Other'
    END AS tier
FROM transactions;

-- Generate a report of the number of loans under each tier group by date
SELECT
    settlement_date,
    tier,
    COUNT(*) AS num_loans
FROM (
    SELECT
        settlement_date,
        CASE
            WHEN total_loan_amount > 100000 THEN 'Tier 1'
            WHEN total_loan_amount > 50000 THEN 'Tier 2'
            WHEN total_loan_amount > 10000 THEN 'Tier 3'
            ELSE 'Other'
        END AS tier
    FROM transactions
) AS tier_data
GROUP BY settlement_date, tier
ORDER BY settlement_date, tier;