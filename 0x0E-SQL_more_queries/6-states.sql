-- Write a script that creates the table force_name on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT UNIQUE AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
