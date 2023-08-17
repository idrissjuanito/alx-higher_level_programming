-- query tv_shows and all genres the blong to
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres
ON id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;
