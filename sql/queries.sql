-- Dengue in Bangladesh (2020-2025): SQL analysis
-- Table: dengue (576 rows; 8 divisions x 72 months)
-- Columns: division, year, month, pollution, density, infected, death,
--          temperature, humidity, pressure, class, date, death_rate, month_num

-- Q1: How many rows are in the table?
SELECT COUNT(*) AS total_rows FROM dengue;

-- Q2: Which division has the most cases and the highest death rate?
SELECT division,
       SUM(infected) AS cases,
       SUM(death) AS deaths,
       ROUND(100.0 * SUM(death) / SUM(infected), 2) AS death_rate_pct
FROM dengue
GROUP BY division
ORDER BY cases DESC;

-- Q3: In which months do cases peak, and what is the climate like?
SELECT month_num,
       SUM(infected) AS cases,
       ROUND(AVG(temperature), 1) AS avg_temp,
       ROUND(AVG(humidity), 2) AS avg_humidity
FROM dengue
GROUP BY month_num
ORDER BY month_num;

-- Q4: How did cases and deaths change year by year?
SELECT year, SUM(infected) AS cases, SUM(death) AS deaths
FROM dengue
GROUP BY year
ORDER BY year;

-- Q5: Which divisions have more than 50,000 total cases?
SELECT division, SUM(infected) AS cases
FROM dengue
GROUP BY division
HAVING SUM(infected) > 50000
ORDER BY cases DESC;

-- Q6: Which 5 division-months had the most cases?
SELECT division, date, infected, death
FROM dengue
ORDER BY infected DESC
LIMIT 5;

-- Q7: What share of all cases does each division account for?
SELECT division,
       SUM(infected) AS cases,
       ROUND(100.0 * SUM(infected) / (SELECT SUM(infected) FROM dengue), 1) AS share_pct
FROM dengue
GROUP BY division
ORDER BY cases DESC;

-- Q8: What share of cases happens in Aug-Nov vs the rest of the year?
SELECT CASE WHEN month_num BETWEEN 8 AND 11 THEN 'Aug-Nov'
            ELSE 'Other months' END AS period,
       SUM(infected) AS cases,
       ROUND(100.0 * SUM(infected) / (SELECT SUM(infected) FROM dengue), 1) AS share_pct
FROM dengue
GROUP BY period;
