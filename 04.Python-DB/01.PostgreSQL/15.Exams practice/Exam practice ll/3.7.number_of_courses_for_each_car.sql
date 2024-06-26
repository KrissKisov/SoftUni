SELECT 
	c.id AS car_id,
	c.make,
	c.mileage,
	COUNT(co.car_id) AS count_of_courses,
	round(AVG(co.bill), 2) AS average_bill
FROM 
	cars AS c
	LEFT JOIN courses AS co
	ON c.id = co.car_id
GROUP BY 
	c.id, c.make, c.mileage
HAVING
	COUNT(car_id) <> 2
ORDER BY
	count_of_courses DESC,
	car_id
;
