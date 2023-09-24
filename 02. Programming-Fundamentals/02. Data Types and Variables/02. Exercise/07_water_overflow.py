number_of_pourings = int(input())
tank_capacity = 255
poured_liters = 0

for pour in range(number_of_pourings):
    liters_of_water = int(input())
    if tank_capacity >= liters_of_water:
        tank_capacity -= liters_of_water
        poured_liters += liters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(poured_liters)
