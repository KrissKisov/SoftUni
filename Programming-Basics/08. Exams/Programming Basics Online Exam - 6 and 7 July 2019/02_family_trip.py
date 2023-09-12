budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percent = int(input())

discount = 5 / 100

total_nights_cost = nights * price_per_night
if nights > 7:
    total_nights_cost -= total_nights_cost * discount

trip_cost = total_nights_cost + budget * additional_expenses_percent / 100

difference = budget - trip_cost

if budget >= trip_cost:
    print(f"Ivanovi will be left with {difference :.2f} leva after vacation.")
else:
    print(f"{abs(difference) :.2f} leva needed.")
