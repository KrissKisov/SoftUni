CREATE OR REPLACE FUNCTION
	udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT AS
$$
BEGIN
	RETURN (
		SELECT
			COUNT(p.id)
		FROM
			accounts AS a
			JOIN accounts_photos AS ap
			ON ap.account_id = a.id
				JOIN photos AS p
				ON p.id = ap.photo_id
		WHERE
			a.username = account_username
	);
END;
$$
LANGUAGE plpgsql;

-- SELECT udf_accounts_photos_count('ssantryd') AS photos_count;
