-- task-5

CREATE TABLE if not EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name varchar(256)
);