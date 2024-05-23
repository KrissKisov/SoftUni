SELECT
	title
FROM
	books
WHERE
	LEFT(title, 3) = 'The'
    -- SUBSTRING(title, 1, 3) = 'The'
ORDER BY
	id
;
