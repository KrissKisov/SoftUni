rows, columns = input().split(",")

rows, columns = int(rows), int(columns)
mouse = None
cheese_to_be_eaten = 0
cupboard = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    current_row = input()

    cupboard.append([x for x in current_row])

    if "M" in current_row:
        mouse = [row, current_row.index("M")]
        cupboard[mouse[0]][mouse[1]] = "*"

    if "C" in current_row:
        cheese_to_be_eaten += current_row.count("C")

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    r, c = mouse[0] + directions[command][0], mouse[1] + directions[command][1]

    if r not in range(rows) or c not in range(columns):
        print("No more cheese for tonight!")
        break

    elif cupboard[r][c] == "@":
        continue

    mouse = r, c

    if cupboard[r][c] == "C":

        cupboard[r][c] = "*"
        cheese_to_be_eaten -= 1

        if not cheese_to_be_eaten:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif cupboard[r][c] == "T":
        print("Mouse is trapped!")
        break

cupboard[mouse[0]][mouse[1]] = "M"

[print(*row, sep="") for row in cupboard]
