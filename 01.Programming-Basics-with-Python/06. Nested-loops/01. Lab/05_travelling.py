destination = input()

while destination != "End":
    trip_coast = float(input())
    saved_money = 0

    while saved_money < trip_coast:
        current_amount = float(input())
        saved_money += current_amount

    if saved_money >= trip_coast:
        print(f"Going to {destination}!")
        saved_money = 0

    destination = input()
