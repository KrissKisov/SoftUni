luggage_capacity = float(input())
command = input()
load_counter = 0
total_loads_count = 0

while command != "End":
    load_volume = float(command)
    load_counter += 1

    if load_counter == 3:
        load_counter = 0
        load_volume *= 1.1

    if luggage_capacity < load_volume:
        break

    luggage_capacity -= load_volume
    total_loads_count += 1

    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {total_loads_count} suitcases loaded.")
