from collections import deque

water_in_dispenser = int(input())
queue = deque()

name = input()
while name != "Start":
    queue.append(name)

    name = input()

command = input()
while command != "End":
    current_command = command.split()
    if len(current_command) == 1:
        liters = int(current_command[0])
        person_in_row = queue.popleft()

        if water_in_dispenser >= liters:
            water_in_dispenser -= liters
            print(f"{person_in_row} got water")
        else:
            print(f"{person_in_row} must wait")

    elif len(current_command) == 2:
        litters_to_refill = int(current_command[1])
        water_in_dispenser += litters_to_refill

    command = input()
print(f"{water_in_dispenser} liters left")
