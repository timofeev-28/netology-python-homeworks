INSERT INTO genres (genre_name)
VALUES
    ('Pop'),
    ('Rock'),
    ('Jazz');

INSERT INTO musicians (musician_name)
VALUES
    ('Michael Jackson'),
    ('Rihanna'),
    ('Metallica'),
    ('Karen Souza'), 
    ('Diana Krall');

INSERT INTO genre_musician (genre_id, musician_id)
VALUES
    (1, 1),
    (1, 2),
    (3, 2),
    (2, 3),
    (3, 4),
    (3, 5);

INSERT INTO albums (album_name, release_date)
VALUES
    ('Bad', DATE '1987-08-25'),
    ('Dangerous', DATE '2020-11-26'),
    ('Loud', DATE '2019-01-01'),
    ('Master of Puppets', DATE '1986-02-12'),
    ('Hotel Souza', DATE '2019-01-01'),
    ('The Look of Love', DATE '2019-01-01');

INSERT INTO discography (musician_id, album_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6);

INSERT INTO tracks (track_name, track_size, album_id)
VALUES
    ('Bad', 247, 1),
    ('Dirty Diana', 281, 1),
    ('Jam', 339, 2),
    ('S&M', 243, 3),
    ('Fading', 199, 3),
    ('Battery', 288, 4),
    ('My Paris', 226, 5),
    ('My own', 249, 5),
    ('Own my', 289, 6),
    ('my', 331, 6),
    ('Oh my god', 245, 6),
    ('myself', 191, 5),
    ('By myself', 289, 5),
    ('bemy self', 256, 5),
    ('myself by', 209, 5),
    ('by myself by', 193, 5),
    ('beemy', 283, 5),
    ('premyne', 227, 5),
    ('Dindi', 239, 5),
    ('Cry Me a River', 305, 6),
    ('Love Letters', 295, 6);

INSERT INTO collections (collection_name, release_date)
VALUES
    ('Best-1', DATE '2018-01-07'),
    ('Best-2', DATE '2020-12-24'),
    ('Pop-Rock', DATE '2026-02-09'),
    ('Best Jazz', DATE '2020-02-09');

INSERT INTO track_collection (track_id, collection_id)
VALUES
    (1, 1),
    (3, 1),
    (5, 1),
    (2, 2),
    (3, 2),
    (4, 2),
    (1, 3),
    (2, 3),
    (5, 3),
    (2, 3),
    (6, 3),
    (7, 4),
    (8, 4),
    (10, 4);
