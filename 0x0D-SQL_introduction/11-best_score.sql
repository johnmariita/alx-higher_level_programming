-- Script that list the rows ordered by score and filtered
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
