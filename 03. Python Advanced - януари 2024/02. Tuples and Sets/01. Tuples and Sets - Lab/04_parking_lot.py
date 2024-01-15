number_of_cars = int(input())
parking_lot = set()

for car in range(number_of_cars):
    in_or_out, number_plate = input().split(", ")
    if in_or_out == "IN":
        parking_lot.add(number_plate)
    elif in_or_out == "OUT":
        parking_lot.discard(number_plate)

if parking_lot:
    for number_plate in parking_lot:
        print(number_plate)
else:
    print("Parking Lot is Empty")
