UPDATE
	books
SET
	title = REPLACE( title, 'The', '***')
WHERE
	LEFT(title, 3) = 'The'
;

SELECT
	title
FROM
	books
WHERE
	title LIKE '***%'
ORDER BY
	id 
;
