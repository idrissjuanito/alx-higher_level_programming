-- query genres of a particular tv_show
SELECT *
FROM tv_genres
INNER JOIN tv_show_genres
ON id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY name;
