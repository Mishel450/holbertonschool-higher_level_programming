-- task-6

CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE if not EXISTS hbtn_0d_usa.states (
    id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(256)
);