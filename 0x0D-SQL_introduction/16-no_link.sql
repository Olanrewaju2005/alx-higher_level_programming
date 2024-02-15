-- Script lists all records of the table second_table
-- Of the database hbtn_0c_0 in my MySQL server
-- Rows without a name value are not listed
-- Records display score and name in this order
-- Results are listed by descending score
-- The database name is passed as an argument to the mysql command
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
