CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE fish (
    id INTEGER PRIMARY KEY,
    fish_name TEXT,
    weight NUMBER,
    user_id INTEGER REFERENCES users
);