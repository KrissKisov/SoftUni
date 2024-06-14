SELECT
	cl.full_name,
	COUNT(co.car_id) AS count_of_cars,
	SUM(co.bill) AS total_sum
FROM
	courses AS co
	JOIN clients AS cl
	ON cl.id = co.client_id
WHERE
	cl.full_name LIKE '_a%'
GROUP BY
	cl.full_name
HAVING
	COUNT(co.car_id) > 1
ORDER BY
	cl.full_name
;
