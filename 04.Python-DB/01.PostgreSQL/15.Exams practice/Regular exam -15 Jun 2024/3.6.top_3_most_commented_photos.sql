SELECT
	p.id as photo_id, 
	capture_date, 
	description,
	COUNT(p.id) AS comments_count

FROM
	photos AS p
	JOIN "comments" as c
	ON c.photo_id = p.id
WHERE
	p.description IS NOT NULL
GROUP BY 
	p.id
ORDER BY 
	comments_count DESC,
	p.id
LIMIT 3
;
