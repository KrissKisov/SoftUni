size = int(input())

fishing_area = []
ship_position = None
fish_quota = 20
caught_fish = 0

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    fishing_area.append([x for x in input()])

    if "S" in fishing_area[row]:
        ship_position = [row, fishing_area[row].index("S")]

command = input()
fell_in_whirlpool = False

while command != "collect the nets":

    fishing_area[ship_position[0]][ship_position[1]] = "-"
    r, c = ship_position[0] + direction[command][0], ship_position[1] + direction[command][1]

    if r not in range(size) or c not in range(size):
        if r < 0:
            r = size - 1
        elif r > size - 1:
            r = 0

        if c < 0:
            c = size - 1
        elif c > size - 1:
            c = 0

    if fishing_area[r][c].isdigit():
        caught_fish += int(fishing_area[r][c])
        fishing_area[r][c] = "S"

    elif fishing_area[r][c] == "W":
        caught_fish = 0
        ship_position = [r, c]
        fishing_area[r][c] = "S"
        fell_in_whirlpool = True
        break

    elif fishing_area[r][c] == "-":
        fishing_area[r][c] = "S"

    ship_position = [r, c]

    command = input()

if fell_in_whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{ship_position[0]},{ship_position[1]}]")
else:

    if caught_fish >= fish_quota:
        print("Success! You managed to reach the quota!")

    else:
        fish_needed = fish_quota - caught_fish
        print(f"You didn't catch enough fish and didn't reach the quota! You need {fish_needed} tons of fish more.")

    if caught_fish > 0:
        print(f"Amount of fish caught: {caught_fish} tons.")

    [print(*row, sep="") for row in fishing_area]
