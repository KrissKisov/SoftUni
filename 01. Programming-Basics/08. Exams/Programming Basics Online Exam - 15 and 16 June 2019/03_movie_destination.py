budget = float(input())
destination = input()  # "Dubai", "Sofia" и "London"
season = input()  # "Summer" и "Winter"
num_days = int(input())

price = 0

if destination == "Dubai":
    if season == "Summer":
        price = 40_000
    else:
        price = 45_000
elif destination == "Sofia":
    if season == "Summer":
        price = 12_500
    else:
        price = 17_000
else:
    if season == "Summer":
        price = 20_250
    else:
        price = 24_000

final_price = num_days * price
if destination == "Dubai":
    final_price *= 0.7
elif destination == "Sofia":
    final_price *= 1.25

difference = budget - final_price

if difference >= 0:
    print(f"The budget for the movie is enough! We have {difference :.2f} leva left!")
else:
    print(f"The director needs {abs(difference) :.2f} leva more!")
