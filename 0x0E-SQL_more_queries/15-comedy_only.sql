-- query tv_shows of a particular genre
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres
ON id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY title;
