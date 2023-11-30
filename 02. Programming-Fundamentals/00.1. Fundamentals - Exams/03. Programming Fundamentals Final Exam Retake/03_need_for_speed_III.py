number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    car_name, mileage, fuel = input().split("|")
    cars.update({car_name: {"mileage": int(mileage), "fuel": int(fuel)}})

command = input().split(" : ")
while command[0] != "Stop":
    action = command[0]
    if action == "Drive":
        car_to_drive, distance, fuel_needed = command[1], int(command[2]), int(command[3])
        if cars[car_to_drive]["fuel"] >= fuel_needed:
            cars[car_to_drive]["mileage"] += distance
            cars[car_to_drive]["fuel"] -= fuel_needed
            print(f"{car_to_drive} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if cars[car_to_drive]["mileage"] >= 100_000:
                # del cars[car_to_drive]
                cars.pop(car_to_drive)
                print(f"Time to sell the {car_to_drive}!")

        else:
            print("Not enough fuel to make that ride")

    elif action == "Refuel":
        car_to_refill, fuel_to_refill = command[1], int(command[2])
        tank_capacity = 75
        possible_refiling = tank_capacity - cars[car_to_refill]["fuel"]
        if possible_refiling >= fuel_to_refill:
            cars[car_to_refill]["fuel"] += fuel_to_refill
            print(f"{car_to_refill} refueled with {fuel_to_refill} liters")
        else:
            cars[car_to_refill]["fuel"] += possible_refiling
            print(f"{car_to_refill} refueled with {possible_refiling} liters")

    elif action == "Revert":
        car_for_reverting, kilometres_to_revert = command[1], int(command[2])
        if cars[car_for_reverting]["mileage"] - kilometres_to_revert < 10000:
            cars[car_for_reverting]["mileage"] = 10000
        else:
            cars[car_for_reverting]["mileage"] -= kilometres_to_revert
            print(f"{car_for_reverting} mileage decreased by {kilometres_to_revert} kilometers")

    command = input().split(" : ")

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
