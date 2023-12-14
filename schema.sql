CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    username TEXT,
    comment TEXT,
    posted TIMESTAMP
);

CREATE TABLE ratings(
    id SERIAL PRIMARY KEY,
    username TEXT,
    rating INTEGER,
    posted TIMESTAMP
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    amount INTEGER,
    ordered TIMESTAMP
);

CREATE TABLE pizza_orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    pizza TEXT
);

CREATE TABLE drink_orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    drink TEXT
);