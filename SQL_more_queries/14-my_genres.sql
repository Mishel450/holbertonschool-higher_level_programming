-- task-14

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
JOIN tv_shows ON tv_show_genres.genre_id = tv_shows.title;
WHERE tv_shows.title = 'Dexter';