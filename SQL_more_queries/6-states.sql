-- task-6

CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE states (
    id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(256)
);