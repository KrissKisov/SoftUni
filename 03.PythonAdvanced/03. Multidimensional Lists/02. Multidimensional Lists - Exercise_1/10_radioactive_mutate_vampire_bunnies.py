rows, columns = [int(x) for x in input().split()]

player_pos = []
bunny_pos = []
lair = []
directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

won_or_dead = ""

for row in range(rows):
    current_row = list(input())
    lair.append(current_row)
    if "P" in current_row:
        player_pos = [row, lair[row].index("P")]
        lair[player_pos[0]][player_pos[1]] = "."

    if "B" in current_row:
        bunny_pos.extend([[row, el] for el in range(columns) if current_row[el] == "B"])

command = input()
for move in command:
    game_is_over = False
    r, c = directions[move][0] + player_pos[0], directions[move][1] + player_pos[1]
    if r not in range(rows) or c not in range(columns):
        won_or_dead = "won"
        game_is_over = True
    else:
        player_pos = [r, c]
        if lair[r][c] == "B":
            won_or_dead = "dead"
            game_is_over = True

    for bunny in bunny_pos:
        for direction in directions.values():
            new_bunny = [bunny[0] + direction[0], bunny[1] + direction[1]]
            if new_bunny == player_pos:
                if won_or_dead != "won":
                    won_or_dead = "dead"
                game_is_over = True

            if new_bunny[0] in range(rows) and new_bunny[1] in range(columns):
                lair[new_bunny[0]][new_bunny[1]] = "B"

    bunny_pos.clear()
    for line in range(rows):
        if "B" in lair[line]:
            bunny_pos.extend([line, x] for x in range(columns) if lair[line][x] == "B")

    if game_is_over:
        break

[print(*row, sep="") for row in lair]
print(f"{won_or_dead}: {player_pos[0]} {player_pos[1]}")
