CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE fish (
    id INTEGER PRIMARY KEY,
    fish_species TEXT,
    fish_length INTEGER,
    catch_location TEXT,
    user_id INTEGER REFERENCES users
);