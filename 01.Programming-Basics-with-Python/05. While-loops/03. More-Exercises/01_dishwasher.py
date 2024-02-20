bottles_detergent = int(input())
available_detergent = int(bottles_detergent * 750)

plate = 5
washed_plates = 0
saucepan = 15
washed_saucepans = 0
loads = 0
command = input()
while command != "End":
    loads += 1
    if loads <= 2:
        available_detergent = available_detergent - int(command) * plate
        washed_plates += int(command)
    elif loads == 3:
        available_detergent = available_detergent - int(command) * saucepan
        washed_saucepans += int(command)
        loads = 0
    if available_detergent < 0:
        break
    command = input()

if command == "End":
    print("Detergent was enough!")
    print(f"{washed_plates} dishes and {washed_saucepans} pots were washed.")
    print(f"Leftover detergent {available_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(available_detergent)} ml. more necessary!")
