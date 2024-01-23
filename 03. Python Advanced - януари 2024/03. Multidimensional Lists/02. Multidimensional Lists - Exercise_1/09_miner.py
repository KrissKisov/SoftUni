size = int(input())
commands = input().split()

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

matrix = []
total_coal = 0
collected_coal = 0
miner_position = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if "c" in line:
        total_coal += line.count("c")

    if "s" in line:
        miner_position = [row, line.index("s")]
        matrix[miner_position[0]][miner_position[1]] = "*"

for command in commands:
    row_to_move, col_to_move = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]
    if row_to_move in range(size) and col_to_move in range(size):
        miner_position = [row_to_move, col_to_move]

        if matrix[row_to_move][col_to_move] == "c":
            collected_coal += 1
            matrix[row_to_move][col_to_move] = "*"

            if collected_coal == total_coal:
                print(f"You collected all coal! ({row_to_move}, {col_to_move})")
                break

        elif matrix[row_to_move][col_to_move] == "e":
            matrix[row_to_move][col_to_move] = "*"
            print(f"Game over! ({row_to_move}, {col_to_move})")
            break
else:
    coals_left = total_coal - collected_coal
    print(f"{coals_left} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
