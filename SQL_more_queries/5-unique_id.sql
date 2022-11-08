-- script that creates the table unique_id on your MySQL server.
-- id INT with the DEFAULT 1 and must be UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
