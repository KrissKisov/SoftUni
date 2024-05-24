SELECT
	first_name,
	last_name,
	-- TO_CHAR(born, 'yyyy') AS "year"
	-- EXTRACT(year FROM born) AS "year"
	date_part('year', born)
FROM
	authors
;
