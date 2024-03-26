-- Script that displays the scores and names from a table
-- Does not display records with missing names
SELECT score, name FROM second_table
	WHERE NAME IS NOT NULL
	ORDER BY score DESC;
