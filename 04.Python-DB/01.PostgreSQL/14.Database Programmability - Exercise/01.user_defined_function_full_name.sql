-- #1
CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(30), last_name VARCHAR(30))
RETURNS VARCHAR(61) AS
$$
	BEGIN
		RETURN CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
	END;
$$
LANGUAGE plpgsql;


-- -- #2
-- CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
-- RETURNS VARCHAR
-- AS
-- $$
-- 	DECLARE
-- 		full_name VARCHAR;
-- 	BEGIN
-- 		full_name := CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
-- 		RETURN full_name;
-- 	END;
-- $$
-- LANGUAGE plpgsql;
