-- Script that displays the average temps in the cities

SELECT city, AVG(value) as avg_temp
	FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
