CREATE OR REPLACE PROCEDURE
	udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
AS
$$
BEGIN
	UPDATE
		accounts
	SET
		job_title = CONCAT('(Remote) ', job_title)
	WHERE id = (
		SELECT
			ac.id
		FROM
			accounts AS ac
			JOIN addresses AS ad
			ON ad.account_id = ac.id
		WHERE
			ad.street = address_street
			AND
			ad.town = address_town
	);
END;
$$
LANGUAGE plpgsql;

-- CALL udp_modify_account('97 Valley Edge Parkway', 'Divinópolis');

-- SELECT a.username, a.gender, a.job_title FROM accounts AS a
-- WHERE a.job_title ILIKE '(Remote)%';
