size = 6
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
matrix = []

for line in range(size):
    matrix.append(input().split())

position = [int(x) for x in input()[1:-1].split(", ")]

command = input().split(", ")

while command[0] != "Stop":
    action, direction = command[0], command[1]
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]

    if action == "Create":
        value = command[2]

        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif action == "Update":
        value = command[2]

        if matrix[row][col] != ".":
            matrix[row][col] = value

    elif action == "Delete":

        if matrix[row][col] != ".":
            matrix[row][col] = "."

    elif action == "Read":

        if matrix[row][col] != ".":
            print(matrix[row][col])

    position = [row, col]

    command = input().split(", ")

[print(*line) for line in matrix]
