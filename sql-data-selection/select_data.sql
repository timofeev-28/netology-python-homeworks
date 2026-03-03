  -- ЗАДАНИЕ 2

-- 1. Название и продолжительность самого длительного трека
SELECT
    track_name,
    CONCAT(
        FLOOR(track_size / 60),
        ':',
        LPAD((track_size % 60)::text, 2, '0')
      ) AS track_size
FROM tracks
WHERE track_size = (SELECT MAX(track_size) FROM tracks);

-- 2. Название треков, продолжительность которых не менее 3,5 минут
SELECT
  track_name,
  CONCAT(
      FLOOR(track_size / 60),
      ':',
      LPAD((track_size % 60)::text, 2, '0')
    ) AS track_size
FROM tracks
WHERE track_size >= 210
ORDER BY track_size;

-- 3. Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT collection_name, release_date
FROM collections
WHERE release_date BETWEEN DATE '2018-01-01' AND DATE '2020-12-31';

-- 4. Исполнители, чьё имя состоит из одного слова
SELECT musician_name
FROM musicians
WHERE musician_name NOT LIKE '% %';

-- 5. Название треков, которые содержат слово «мой» или «my»
SELECT track_name
FROM tracks
WHERE track_name ILIKE 'my' 
   OR track_name ILIKE 'my %' 
   OR track_name ILIKE '% my' 
   OR track_name ILIKE '% my %'
   OR track_name ILIKE 'мой'
   OR track_name ILIKE 'мой %'
   OR track_name ILIKE '% мой'
   OR track_name ILIKE '% мой %';


   -- ЗАДАНИЕ 3

-- 1. Количество исполнителей в каждом жанре
SELECT g.genre_name, COUNT(gm.musician_id) AS musician_total
FROM genres AS g
LEFT JOIN genre_musician AS gm ON gm.genre_id = g.genre_id
GROUP BY g.genre_name;

-- 2. Количество треков в альбомах 2019–2020
SELECT COUNT(t.track_id) AS tracks_total
FROM tracks AS t
LEFT JOIN albums AS a ON t.album_id = a.album_id
WHERE a.release_date BETWEEN DATE '2019-01-01' AND DATE '2020-12-31';

-- 3. Средняя продолжительность треков по каждому альбому
SELECT
    a.album_name,
    CONCAT(
        FLOOR(AVG(t.track_size) / 60),
        ':',
        TO_CHAR(FLOOR(AVG(t.track_size) % 60), 'FM00')
      ) AS mean_size
FROM albums a 
LEFT JOIN tracks t ON t.album_id = a.album_id
GROUP BY a.album_name
ORDER BY mean_size DESC;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году
SELECT m.musician_name
FROM musicians m
WHERE m.musician_name NOT IN (
    SELECT m.musician_name
    FROM musicians m
    JOIN discography d ON d.musician_id  = m.musician_id
    JOIN albums a ON a.album_id = d.album_id
    WHERE EXTRACT(YEAR FROM a.release_date) = 2020
);

-- 5. Названия сборников, в которых присутствует конкретный исполнитель (Diana Krall)
SELECT c.collection_name
FROM collections c
JOIN track_collection tc ON tc.collection_id  = c.collection_id
JOIN tracks t ON t.track_id = tc.track_id
JOIN albums a ON a.album_id  = t.album_id
JOIN discography d ON d.album_id  = a.album_id
JOIN musicians m  ON m.musician_id  = d.musician_id
WHERE m.musician_name  = 'Diana Krall';
