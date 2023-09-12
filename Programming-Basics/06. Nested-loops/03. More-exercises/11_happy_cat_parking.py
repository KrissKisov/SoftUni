number_of_days = int(input())
number_of_hours = int(input())
price_per_day = 0
total_amount = 0
for day in range(1, number_of_days + 1):
    price_per_day = 0
    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            current_price = 1.25
        else:
            current_price = 1

        price_per_day += current_price

    print(f"Day: {day} - {price_per_day :.2f} leva")
    total_amount += price_per_day
print(f"Total: {total_amount :.2f} leva")
