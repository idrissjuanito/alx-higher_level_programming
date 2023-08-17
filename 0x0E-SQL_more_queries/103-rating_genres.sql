-- select genres and the sum of their ratings
SELECT name, SUM(rate) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
