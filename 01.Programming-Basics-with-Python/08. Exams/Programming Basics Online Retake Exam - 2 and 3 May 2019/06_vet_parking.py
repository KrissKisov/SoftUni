num_days = int(input())
num_hours = int(input())
total_parking_fee = 0
fee_per_day = 0
fee_per_hour = 0
for day in range(1, num_days + 1):
    for hour in range(1, num_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            fee_per_hour = 2.5

        elif day % 2 != 0 and hour % 2 == 0:
            fee_per_hour = 1.25

        else:
            fee_per_hour = 1

        fee_per_day += fee_per_hour

    total_parking_fee += fee_per_day
    print(f"Day: {day} - {fee_per_day :.2f} leva")
    fee_per_day = 0

print(f"Total: {total_parking_fee :.2f} leva")
