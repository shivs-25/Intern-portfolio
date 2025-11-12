-- Bellabeat Fitness Data SQL Analysis

-- 1️. Total unique users
SELECT COUNT(DISTINCT Id) AS total_users
FROM daily_activity;

-- 2️. Average daily steps and calories per user
SELECT Id,
       ROUND(AVG(TotalSteps), 0) AS avg_steps,
       ROUND(AVG(Calories), 0) AS avg_calories
FROM daily_activity
GROUP BY Id
ORDER BY avg_steps DESC
LIMIT 10;

-- 3️. Average steps and calories by weekday
SELECT STRFTIME('%w', ActivityDate) AS weekday_number,
       CASE STRFTIME('%w', ActivityDate)
            WHEN '0' THEN 'Sunday'
            WHEN '1' THEN 'Monday'
            WHEN '2' THEN 'Tuesday'
            WHEN '3' THEN 'Wednesday'
            WHEN '4' THEN 'Thursday'
            WHEN '5' THEN 'Friday'
            WHEN '6' THEN 'Saturday'
       END AS weekday_name,
       ROUND(AVG(TotalSteps), 0) AS avg_steps,
       ROUND(AVG(Calories), 0) AS avg_calories
FROM daily_activity
GROUP BY weekday_number
ORDER BY weekday_number;

-- 4️. Average sleep hours per user
SELECT Id,
       ROUND(AVG(TotalMinutesAsleep) / 60.0, 2) AS avg_sleep_hours
FROM daily_activity
WHERE TotalMinutesAsleep > 0
GROUP BY Id
ORDER BY avg_sleep_hours DESC
LIMIT 10;

-- 5️. Correlation query (this can be run in Python if not supported by DB)
SELECT ROUND(CORR(TotalSteps, Calories), 3) AS corr_steps_calories FROM daily_activity;
