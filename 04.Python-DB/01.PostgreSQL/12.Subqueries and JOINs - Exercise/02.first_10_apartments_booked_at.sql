SELECT 
	a."name"
	,a.country
	,DATE(b.booked_at) -- also valid: 'b.booked_at::DATE', 'TO_CHAR(b.booked_at, 'YYYY-MM-DD')'
FROM 
	apartments AS a
	LEFT JOIN 
		bookings AS b
	on 
		a.booking_id = b.booking_id
LIMIT 10
;
