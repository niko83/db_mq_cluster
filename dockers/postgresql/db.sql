CREATE TABLE users (
    uuid uuid,
    email text UNIQUE,
    score bigint default 0,
    created_at timestamp default NOW(),
    PRIMARY KEY (uuid)
);
