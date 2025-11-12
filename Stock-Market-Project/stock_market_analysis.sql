-- Stock Market Analysis SQL Script


-- Query: trend_percentage_change
WITH bounds AS (
  SELECT company, MIN(date) AS start_date, MAX(date) AS end_date
  FROM stock_prices GROUP BY company
),
ends AS (
  SELECT b.company, b.start_date, b.end_date,
         s.close AS start_close, e.close AS end_close
  FROM bounds b
  JOIN stock_prices s ON s.company=b.company AND s.date=b.start_date
  JOIN stock_prices e ON e.company=b.company AND e.date=b.end_date
)
SELECT company, start_date, end_date, start_close, end_close,
       ROUND(((end_close - start_close)/start_close)*100.0, 2) AS percent_change
FROM ends
ORDER BY percent_change DESC;;

-- Query: trend_fixed_window
WITH windowed AS (
  SELECT company, date, close
  FROM stock_prices
  WHERE date BETWEEN DATE('2015-01-01') AND DATE('2018-07-31')
),
bounds AS (
  SELECT company, MIN(date) AS start_date, MAX(date) AS end_date
  FROM windowed GROUP BY company
),
ends AS (
  SELECT b.company, b.start_date, b.end_date,
         s1.close AS start_close, s2.close AS end_close
  FROM bounds b
  LEFT JOIN windowed s1 ON s1.company=b.company AND s1.date=b.start_date
  LEFT JOIN windowed s2 ON s2.company=b.company AND s2.date=b.end_date
)
SELECT company, start_date, end_date, start_close, end_close,
       CASE WHEN start_close IS NULL OR end_close IS NULL THEN NULL
            ELSE ROUND(((end_close - start_close)/start_close)*100.0, 2) END AS percent_change
FROM ends
ORDER BY percent_change DESC;;

-- Query: buy_sell_signals
WITH ordered AS (
  SELECT company, date, close,
         LAG(close,1) OVER (PARTITION BY company ORDER BY date) AS c1,
         LAG(close,2) OVER (PARTITION BY company ORDER BY date) AS c2
  FROM stock_prices
),
signals AS (
  SELECT company, date, close,
         CASE
           WHEN close > c1 AND c1 > c2 THEN 'BUY'
           WHEN close < c1 AND c1 < c2 THEN 'SELL'
           ELSE 'HOLD'
         END AS signal
  FROM ordered
)
SELECT * FROM signals
ORDER BY company, date;;

-- Query: latest_recommendation
WITH ordered AS (
  SELECT company, date, close,
         LAG(close,1) OVER (PARTITION BY company ORDER BY date) AS c1,
         LAG(close,2) OVER (PARTITION BY company ORDER BY date) AS c2
  FROM stock_prices
),
signals AS (
  SELECT company, date, close,
         CASE
           WHEN close > c1 AND c1 > c2 THEN 'BUY'
           WHEN close < c1 AND c1 < c2 THEN 'SELL'
           ELSE 'HOLD'
         END AS signal
  FROM ordered
),
last_sig AS (
  SELECT s.* FROM (
    SELECT company, date, close, signal,
           ROW_NUMBER() OVER (PARTITION BY company ORDER BY date DESC) AS rn
    FROM signals
  ) s WHERE rn=1
),
trend AS (
  WITH bounds AS (
    SELECT company, MIN(date) AS start_date, MAX(date) AS end_date
    FROM stock_prices GROUP BY company
  )
  SELECT b.company,
         ROUND(((e.close - s.close)/s.close)*100.0, 2) AS overall_percent_change
  FROM bounds b
  JOIN stock_prices s ON s.company=b.company AND s.date=b.start_date
  JOIN stock_prices e ON e.company=b.company AND e.date=b.end_date
)
SELECT l.company, l.date AS latest_date, l.close AS latest_close, l.signal AS latest_signal,
       t.overall_percent_change,
       CASE
         WHEN l.signal='BUY' AND t.overall_percent_change >= 0 THEN 'BUY'
         WHEN l.signal='SELL' AND t.overall_percent_change < 0 THEN 'SELL'
         ELSE 'HOLD'
       END AS recommendation
FROM last_sig l
JOIN trend t ON t.company=l.company
ORDER BY l.company;;

-- Query: max_min_close
SELECT company, MIN(close) AS min_close, MAX(close) AS max_close
FROM stock_prices GROUP BY company ORDER BY company;;

-- Query: opportunities_sql_note
WITH w AS (
  SELECT company, date, close,
         LAG(close) OVER (PARTITION BY company ORDER BY date) AS prev_close,
         LEAD(close) OVER (PARTITION BY company ORDER BY date) AS next_close
  FROM stock_prices
),
extrema AS (
  SELECT company, date, close,
         CASE
           WHEN (prev_close IS NULL OR close <= prev_close)
                AND (next_close IS NOT NULL AND close < next_close) THEN 'BUY_POINT'
           WHEN (next_close IS NULL OR close >= next_close)
                AND (prev_close IS NOT NULL AND close > prev_close) THEN 'SELL_POINT'
           ELSE NULL
         END AS point_type
  FROM w
)
SELECT company,
       SUM(CASE WHEN point_type='BUY_POINT' THEN 1 ELSE 0 END) AS buy_points,
       SUM(CASE WHEN point_type='SELL_POINT' THEN 1 ELSE 0 END) AS sell_points
FROM extrema
GROUP BY company
ORDER BY company;;

-- Query: percent_change_rank
WITH bounds AS (
  SELECT company, MIN(date) AS start_date, MAX(date) AS end_date
  FROM stock_prices GROUP BY company
),
ends AS (
  SELECT b.company, s.close AS start_close, e.close AS end_close
  FROM bounds b
  JOIN stock_prices s ON s.company=b.company AND s.date=b.start_date
  JOIN stock_prices e ON e.company=b.company AND e.date=b.end_date
)
SELECT company,
       ROUND(((end_close - start_close)/start_close)*100.0, 2) AS percent_change,
       RANK() OVER (ORDER BY ((end_close - start_close)/start_close) DESC) AS rank_by_growth
FROM ends
ORDER BY rank_by_growth;;

