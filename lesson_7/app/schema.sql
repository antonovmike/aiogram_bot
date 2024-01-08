CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id TEXT
);
CREATE TABLE IF NOT EXISTS items(
    i_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    desc TEXT,
    price TEXT,
    photo TEXT,
    brand TEXT
);