-- Write a script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
