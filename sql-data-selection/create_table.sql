-- БД для музыкального сервиса

CREATE TABLE IF NOT EXISTS genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS musicians (
    musician_id SERIAL PRIMARY KEY,
    musician_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(250) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS tracks (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(250) NOT NULL,
    track_size INT CHECK (track_size > 0),
    album_id INT REFERENCES albums(album_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS collections (
    collection_id SERIAL PRIMARY KEY,
    collection_name VARCHAR(250) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS genre_musician (
    genre_musician_id SERIAL PRIMARY KEY,
    genre_id INT REFERENCES genres(genre_id) ON DELETE CASCADE NOT NULL,
    musician_id INT REFERENCES musicians(musician_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS discography (
    discography_id SERIAL PRIMARY KEY,
    musician_id INT REFERENCES musicians(musician_id) ON DELETE CASCADE NOT NULL,
    album_id INT REFERENCES albums(album_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS track_collection (
    track_collection_id SERIAL PRIMARY KEY,
    track_id INT REFERENCES tracks(track_id) ON DELETE CASCADE NOT NULL,
    collection_id INT REFERENCES collections(collection_id) ON DELETE CASCADE NOT NULL
);
