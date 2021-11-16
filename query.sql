WITH p1 AS 
    (SELECT name, high, ts, SUBSTRING(ts,12,2) AS Hour
     FROM sta9760s2021bucket), 
     p2 AS 
    (SELECT p1.name AS Company, MAX(p1.high) AS Highest_Price, p1.Hour
     FROM p1     
     GROUP BY  p1.name, p1.Hour)
    
SELECT p2.Company, p2.Highest_Price, ts AS time, p2.Hour
FROM p1, p2
WHERE p1.name = p2.Company
  AND p1.high = p2.Highest_Price

ORDER BY  p2.Company, p2.Hour 