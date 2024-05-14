rows, columns = [int(x) for x in input().split()]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

playground = []
current_position = None
opponents_num = 0
made_moves = 0
touched_opponents = 0

for i in range(rows):
    row_input = input().split()
    playground.append(row_input)

    if "B" in row_input:
        current_position = [i, row_input.index("B")]

    if "P" in row_input:
        opponents_num += row_input.count("P")

command = input()

while command != "Finish":

    r, c = current_position[0] + directions[command][0], current_position[1] + directions[command][1]

    if r not in range(rows) or c not in range(columns):
        command = input()
        continue

    elif playground[r][c] == "O":
        command = input()
        continue

    elif playground[r][c] == "P":
        made_moves += 1
        touched_opponents += 1
        playground[r][c] = "-"

        if touched_opponents == opponents_num:
            break

    else:
        made_moves += 1

    current_position = [r, c]

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {made_moves}")
