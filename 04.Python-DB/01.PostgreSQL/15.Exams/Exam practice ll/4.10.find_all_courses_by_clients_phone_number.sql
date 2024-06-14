CREATE OR REPLACE FUNCTION 
	fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT AS
$$
BEGIN
	RETURN (
		SELECT
			COUNT(co.id)
		FROM
			courses AS co
			JOIN clients AS cl
			ON cl.id = co.client_id
		WHERE
			cl.phone_number = phone_num
		);
END;
$$
LANGUAGE plpgsql;
