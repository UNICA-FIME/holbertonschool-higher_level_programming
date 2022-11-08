-- 1 creates the database hbtn_0d_usa
-- 2 database selected
-- 3 creates the table states
-- 3.1 id (PK) and auto generated (AUTO_INCREMENT)
-- 3.2 name can’t be null 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
