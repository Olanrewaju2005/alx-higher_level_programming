-- Script lists the number of records with the same score
-- In the table second_table of the database hbtn_0c_0 in my MySQL server
-- The result will display the score
-- It will also display the number of records with the score with the label number
SELECT `score`,
COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
