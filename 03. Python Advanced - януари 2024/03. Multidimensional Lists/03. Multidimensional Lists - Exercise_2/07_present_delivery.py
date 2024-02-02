number_presents = int(input())
size = int(input())

neighborhood = []
santa = []
total_nice_kids = 0
nice_kids_got_presents = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for line in range(size):
    neighborhood.append(input().split())

    if "S" in neighborhood[line]:
        santa = [line, neighborhood[line].index("S")]

    if "V" in neighborhood[line]:
        total_nice_kids += neighborhood[line].count("V")

while True:
    command = input()

    if command == "Christmas morning":
        break

    if number_presents <= 0:
        break

    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]

    if r not in range(size) or c not in range(size):
        break

    neighborhood[santa[0]][santa[1]] = "-"
    santa = [r, c]

    if neighborhood[r][c] == "V":
        neighborhood[santa[0]][santa[1]] = "-"
        number_presents -= 1
        nice_kids_got_presents += 1
        if number_presents <= 0:
            break

    elif neighborhood[r][c] == "X":
        neighborhood[santa[0]][santa[1]] = "-"

    elif neighborhood[r][c] == "C":
        for direction in directions.keys():
            row, col = r + directions[direction][0], c + directions[direction][1]
            if row in range(size) and col in range(size):
                if neighborhood[row][col] == "V":
                    number_presents -= 1
                    nice_kids_got_presents += 1

                elif neighborhood[row][col] == "X":
                    number_presents -= 1

            neighborhood[row][col] = "-"

neighborhood[santa[0]][santa[1]] = "S"

if number_presents <= 0 and nice_kids_got_presents < total_nice_kids:
    print("Santa ran out of presents!")

[print(*line) for line in neighborhood]

if nice_kids_got_presents < total_nice_kids:
    print(f"No presents for {total_nice_kids - nice_kids_got_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
