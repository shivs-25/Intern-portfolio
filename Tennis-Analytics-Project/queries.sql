-- 1) Competitions Analysis: List all competitions with category names
SELECT c.competition_id, c.competition_name, cat.category_name, c.type, c.gender
FROM competitions c
JOIN categories cat ON c.category_id = cat.category_id;

-- 2) Count competitions per category
SELECT cat.category_name, COUNT(*) AS competition_count
FROM competitions c
JOIN categories cat ON c.category_id = cat.category_id
GROUP BY cat.category_name;

-- 3) Top 10 players by points
SELECT competitor_name, rank, points
FROM competitor_rankings
ORDER BY points DESC
LIMIT 10;

-- 4) Average points by country
SELECT country, AVG(points) AS avg_points
FROM competitor_rankings
GROUP BY country
ORDER BY avg_points DESC;

-- 5) Seasonal growth trend
SELECT year, COUNT(season_id) AS total_seasons
FROM seasons
GROUP BY year
ORDER BY year;

-- 6) Players with no rank movement
SELECT competitor_name, rank, movement
FROM competitor_rankings
WHERE movement = 0;

-- 7) Top countries by player representation
SELECT country, COUNT(*) AS player_count
FROM competitor_rankings
GROUP BY country
ORDER BY player_count DESC;
