-- query genres that have 1 or shows and count number of shows
SELECT name AS genre, COUNT(name) AS number_of_shows
FROM tv_genres
FULL JOIN tv_show_genres
ON id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
