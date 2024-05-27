SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	companion_full_name ILIKE '%aNd%' -- 'ILIKE' - case-insensitive
	AND
	email NOT LIKE '%@gmail' -- 'LIKE' - case-sensitive
;