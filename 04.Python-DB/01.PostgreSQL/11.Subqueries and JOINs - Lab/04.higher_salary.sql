SELECT 
	COUNT(*) 
FROM
	employees
WHERE 
	salary > (
		SELECT
			AVG(salary) AS average_salary
		FROM
			employees
	)
;
