guest_number = int(input())
price_per_guest = float(input())
budget = float(input())
cake_price = budget * 0.1

if 10 <= guest_number <= 15:
    price_per_guest *= 0.85
elif 15 < guest_number <= 20:
    price_per_guest *= 0.8
elif guest_number > 20:
    price_per_guest *= 0.75

total_cost = guest_number * price_per_guest + cake_price
difference = budget - total_cost

if budget >= total_cost:
    print(f"It is party time! {difference :.2f} leva left.")
else:
    print(f"No party! {abs(difference) :.2f} leva needed.")
