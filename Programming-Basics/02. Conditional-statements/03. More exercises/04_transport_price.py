kilometers = int(input())
traveling_through = input()

taxi_start_tariff = 0.70
taxi_day_tariff = 0.79
taxi_night_tariff = 0.90
bus_tariff = 0.09
train_tariff = 0.06
taxi_day_price = taxi_start_tariff + taxi_day_tariff * kilometers
taxi_night_price = taxi_start_tariff + taxi_night_tariff * kilometers
bus_price = bus_tariff * kilometers
train_price = train_tariff * kilometers

if kilometers >= 100:
    print(f"{train_price:.2f}")
elif kilometers >= 20:
    print(f"{bus_price:.2f}")
else:
    if traveling_through == "day_of_week":
        print(f"{taxi_day_price:.2f}")
    elif traveling_through == "night":
        print(f"{taxi_night_price:.2f}")
