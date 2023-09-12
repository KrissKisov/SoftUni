price_over_20_kg = float(input())
luggage_in_kg = float(input())
days_before_trip = int(input())
number_luggage = int(input())

luggage_price = 0
if luggage_in_kg < 10:
    luggage_price = price_over_20_kg * 0.2
elif luggage_in_kg <= 20:
    luggage_price = price_over_20_kg * 0.5
else:
    luggage_price = price_over_20_kg

# luggage_price = 0
if days_before_trip < 7:
    luggage_price += luggage_price * 0.4
elif days_before_trip <= 30:
    luggage_price += luggage_price * 0.15
else:
    luggage_price += luggage_price * 0.1

final_price = luggage_price * number_luggage
print(f"The total price of bags is: {final_price :.2f} lv.")
