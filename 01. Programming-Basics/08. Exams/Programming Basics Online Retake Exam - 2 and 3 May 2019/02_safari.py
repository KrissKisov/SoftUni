budget = float(input())
fuel_needed = float(input())
day = input()  # "Saturday" и "Sunday"
fuel_price = 2.10
tour_guide_price = 100
safari_price = tour_guide_price + fuel_needed * fuel_price

if day == "Saturday":
    safari_price *= 0.9
elif day == "Sunday":
    safari_price *= 0.8

difference = budget - safari_price
if budget >= safari_price:
    print(f"Safari time! Money left: {difference :.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(difference) :.2f} lv.")
