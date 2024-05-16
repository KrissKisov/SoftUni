CREATE VIEW highest_paid_employee AS
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 1
;

SELECT * FROM highest_paid_employee;
