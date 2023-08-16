-- finds the max value of grouped data
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;
