size = int(input())
moves = input().split(", ")

collected_hazelnuts = 0
squirrel_pos = []
field = []

for i in range(size):
    field.append(list(input()))

    if "s" in field[i]:
        squirrel_pos = [i, field[i].index("s")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for move in moves:
    r, c = squirrel_pos[0] + directions[move][0], squirrel_pos[1] + directions[move][1]

    if r not in range(size) or c not in range(size):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        exit()

    elif field[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        exit()

    elif field[r][c] == "h":
        collected_hazelnuts += 1
        field[r][c] = "*"

    if collected_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        exit()

    squirrel_pos = [r, c]

print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")
