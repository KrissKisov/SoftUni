SELECT
	-- RIGHT(description, -4)
	SUBSTRING(description, 5)
	-- SUBSTRING(description FROM 5)
FROM
	currencies
;
