-- БД для музыкального сервиса

CREATE TABLE IF NOT EXISTS Genres (
    genre_id SERIAL PRIMARY KEY,
    name_genre VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Musicians (
    musician_id SERIAL PRIMARY KEY,
    name_musician VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Albums (
    album_id SERIAL PRIMARY KEY,
    title_album VARCHAR(250) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Tracks (
    track_id SERIAL PRIMARY KEY,
    title_track VARCHAR(250) NOT NULL,
    length_track INT CHECK (length_track > 0),
    album_id INT REFERENCES Albums(album_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS Collections (
    collection_id SERIAL PRIMARY KEY,
    title_collection VARCHAR(250) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre_Musician (
    genre_musician_id SERIAL PRIMARY KEY,
    genre_id INT REFERENCES Genres(genre_id) ON DELETE CASCADE NOT NULL,
    musician_id INT REFERENCES Musicians(musician_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS Musician_Album (
    musician_album_id SERIAL PRIMARY KEY,
    musician_id INT REFERENCES Musicians(musician_id) ON DELETE CASCADE NOT NULL,
    album_id INT REFERENCES Albums(album_id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE IF NOT EXISTS Track_Collection (
    track_collection_id SERIAL PRIMARY KEY,
    track_id INT REFERENCES Tracks(track_id) ON DELETE CASCADE NOT NULL,
    collection_id INT REFERENCES Collections(collection_id) ON DELETE CASCADE NOT NULL
);
