-- display partial info grouped by and filtered
SELECT city, AVG(value) AS temp_avg FROM temperatures WHERE month = "july" OR month = "august" GROUP BY city ORDER BY temp_avg DESC LIMIT 3;
