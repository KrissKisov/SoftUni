CREATE OR REPLACE PROCEDURE 
	sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC(4))
AS
$$
	DECLARE
		sender_current_balance NUMERIC;
	BEGIN
		sender_current_balance := (SELECT balance FROM accounts WHERE id = sender_id);

		IF sender_current_balance < amount THEN
			-- ROLLBACK;
			RAISE EXCEPTION 'Insufficient balance to withdraw %', amount;

		ELSE
			CALL sp_withdraw_money(sender_id, amount);
			CALL sp_deposit_money(receiver_id, amount);
		END IF;
	END;
$$
LANGUAGE plpgsql;
