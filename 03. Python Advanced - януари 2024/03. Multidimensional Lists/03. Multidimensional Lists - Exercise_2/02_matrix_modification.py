rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    # action, row, col, value = command.split()
    # row, col, value = int(row), int(col), int(value)

    if row not in range(rows) or col not in range(rows):
        print("Invalid coordinates")

    elif action == "Add":
        matrix[row][col] += value

    elif action == "Subtract":
        matrix[row][col] -= value

    command = input()

[print(*line) for line in matrix]
