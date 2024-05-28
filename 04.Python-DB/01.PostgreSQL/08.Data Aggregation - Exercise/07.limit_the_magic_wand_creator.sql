SELECT
	magic_wand_creator,
	-- MIN(magic_wand_size)  -- #1
	MIN(magic_wand_size) AS minimum_wand_size  -- #2
FROM
	wizard_deposits
GROUP BY
	magic_wand_creator
ORDER BY
	-- MIN(magic_wand_size)  -- #1
	minimum_wand_size  -- #2
LIMIT 5
;
