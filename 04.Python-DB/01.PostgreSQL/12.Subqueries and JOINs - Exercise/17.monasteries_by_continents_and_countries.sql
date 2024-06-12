UPDATE 
	countries 
SET 
	country_name = 'Burma'
WHERE 
	country_name = 'Myanmar'
;

INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	('Hanga Abbey', (
					SELECT 
						country_code
					FROM
						countries
					WHERE
						country_name = 'Tanzania'
					))
	,('Myin-Tin-Daik', (
						SELECT 
							country_code
						FROM
							countries
						WHERE
							country_name = 'Myanmar'
						))
;

SELECT
	cont.continent_name
	,coun.country_name
	,COUNT(m.country_code) AS monasteries_count
FROM
	continents AS cont
	JOIN 
		countries AS coun
	USING
		(continent_code)
		LEFT JOIN
			monasteries AS m
		USING
			(country_code)
WHERE
	coun.three_rivers <> TRUE
GROUP BY
	cont.continent_name
	,coun.country_name
ORDER BY 
	monasteries_count DESC
	,coun.country_name
;
