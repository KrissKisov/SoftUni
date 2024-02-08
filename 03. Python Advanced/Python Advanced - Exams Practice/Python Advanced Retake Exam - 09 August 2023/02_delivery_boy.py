rows, columns = [int(x) for x in input().split()]

start_position = []
neighborhood = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    neighborhood.append([x for x in input()])

    if "B" in neighborhood[row]:
        start_position = [row, neighborhood[row].index("B")]

current_position = start_position

while True:
    command = input()

    if not command:
        break

    r, c = current_position[0] + directions[command][0], current_position[1] + directions[command][1]

    if r not in range(rows) or c not in range(columns):
        print("The delivery is late. Order is canceled.")
        neighborhood[start_position[0]][start_position[1]] = " "
        break

    elif neighborhood[r][c] == "*":
        continue

    elif neighborhood[r][c] == "P":
        neighborhood[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif neighborhood[r][c] == "A":
        neighborhood[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif neighborhood[r][c] == "-":
        neighborhood[r][c] = "."

    current_position = [r, c]

[print(*row, sep="") for row in neighborhood]
