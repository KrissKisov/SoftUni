CREATE VIEW continent_currency_usage
AS
SELECT
	ru.continent_code
	,ru.currency_code
	,ru.currency_usage
FROM (
	SELECT
		cu.continent_code
		,cu.currency_code
		,cu.currency_usage
		,DENSE_RANK() OVER(PARTITION BY cu.continent_code ORDER BY cu.currency_usage DESC) AS ranked_usage
	FROM 
		(SELECT 
			continent_code
			,currency_code
			,COUNT(*) AS currency_usage
		FROM
			countries
		GROUP BY
			continent_code
			,currency_code
		HAVING
			COUNT(*) > 1
		ORDER BY 
			currency_usage DESC) AS cu
	) AS ru
WHERE
	ru.ranked_usage = 1
ORDER BY
	ru.currency_usage DESC
	,ru.continent_code
	,ru.currency_code
;

