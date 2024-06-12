CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT AS
$$
	DECLARE
		employee_count INT;
	BEGIN
		RETURN 
			(SELECT
					COUNT(e.employee_id)
				FROM 
					employees AS e
					JOIN addresses AS a
					USING (address_id)
						JOIN towns AS t
						USING (town_id)
				WHERE
					t."name" = town_name);
	END;
$$
LANGUAGE plpgsql;

-- SELECT * FROM fn_count_employees_by_town('Sofia');