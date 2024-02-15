-- Script creates a table in the current database in my MySQL server
-- Database name will be passed as an argument of tht mysql command
-- Script will not fail if the table already exists
USE `hbtn_0c_0`

CREATE TABLE IF NOT EXISTS first_table(
		id INT,
		name VARCHAR(256)
		);
