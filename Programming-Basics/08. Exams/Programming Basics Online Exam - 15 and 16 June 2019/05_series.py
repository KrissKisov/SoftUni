budget = float(input())
number_of_series = int(input())
amount_needed = 0

for _ in range(number_of_series):
    series_name = input()
    price = float(input())

    if series_name == "Thrones":
        price *= 0.5
    elif series_name == "Lucifer":
        price *= 0.6
    elif series_name == "Protector":
        price *= 0.7
    elif series_name == "TotalDrama":
        price *= 0.8
    elif series_name == "Area":
        price *= 0.9

    amount_needed += price

difference = budget - amount_needed

if budget >= amount_needed:
    print(f"You bought all the series and left with {difference :.2f} lv.")
else:
    print(f"You need {abs(difference) :.2f} lv. more to buy the series!")
