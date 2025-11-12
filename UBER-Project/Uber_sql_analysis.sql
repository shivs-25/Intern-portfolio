-- Uber Supply-Demand Gap SQL Analysis
-- Author: Shivali Muthukumar

-- 1. Total Requests by Status
SELECT Status, COUNT(*) AS Total_Requests
FROM uber_requests
GROUP BY Status;

-- 2. Hourly Supply vs Demand Gap
-- Note: Optional visualization step; "None" hour is acceptable due to format differences.
SELECT strftime('%H', "Request timestamp") AS Hour,
       SUM(CASE WHEN Status='Trip Completed' THEN 1 ELSE 0 END) AS Supply,
       SUM(CASE WHEN Status!='Trip Completed' THEN 1 ELSE 0 END) AS Demand_Gap
FROM uber_requests
GROUP BY Hour
ORDER BY Hour;

-- 3. Requests by Pickup Point
SELECT "Pickup point",
       SUM(CASE WHEN Status='Trip Completed' THEN 1 ELSE 0 END) AS Completed,
       SUM(CASE WHEN Status='Cancelled' THEN 1 ELSE 0 END) AS Cancelled,
       SUM(CASE WHEN Status='No Cars Available' THEN 1 ELSE 0 END) AS No_Cars
FROM uber_requests
GROUP BY "Pickup point";

-- 4. Supply-Demand Gap Percentage
SELECT "Pickup point",
       COUNT(*) AS Total_Requests,
       SUM(CASE WHEN Status='Trip Completed' THEN 1 ELSE 0 END) AS Completed,
       ROUND(100.0 * SUM(CASE WHEN Status!='Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS Gap_Percentage
FROM uber_requests
GROUP BY "Pickup point";
