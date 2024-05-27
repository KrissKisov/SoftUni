SELECT 
	department_id,
	COUNT(e.id) AS employee_count
FROM 
	employees AS e
GROUP BY
	department_id
ORDER BY
	department_id
;
