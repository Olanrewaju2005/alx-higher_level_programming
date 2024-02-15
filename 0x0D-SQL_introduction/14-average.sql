-- Script computes the score average of all records
-- In the table second_table of the database hbtn_0c_0 in my MySQL server
-- The result column name will be average
-- The database name will be passed as an argument of the mysql command
SELECT AVG(`score`) AS `average`
FROM `second_table`;
