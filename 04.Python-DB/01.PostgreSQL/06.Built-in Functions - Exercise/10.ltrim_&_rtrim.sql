SELECT 
	-- LTRIM(peak_name, 'M') AS left_trim,
	-- RTRIM(peak_name, 'm') AS right_trim
	TRIM(LEADING 'M' FROM peak_name) AS left_trim,
	TRIM(TRAILING 'm' FROM peak_name) AS right_trim
FROM 
	peaks
;
