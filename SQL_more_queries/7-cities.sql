-- task-7

CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE if not EXISTS hbtn_0d_usa.cities (
    id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id int NOT NULL, 
    FOREIGN KEY (state_id) REFERENCES states(id),
    name varchar(256) NOT NULL
);