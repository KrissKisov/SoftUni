number = int(input())

matrix = []
bunny = []
total_eggs = 0
best_path = {}

for row in range(number):
    line = input().split()
    matrix.append(line)

    if "B" in line:
        bunny = [row, line.index("B")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for direction, indices in directions.items():
    r, c = bunny[0] + indices[0], bunny[1] + indices[1]
    current_path = {}
    collected_eggs = 0

    while r in range(number) and c in range(number):
        if matrix[r][c] == "X":
            break

        collected_eggs += int(matrix[r][c])

        if direction not in current_path.keys():
            current_path[direction] = []
        current_path[direction].append([r, c])
        r += indices[0]
        c += indices[1]

    if collected_eggs >= total_eggs:
        total_eggs = collected_eggs
        best_path = current_path

best_direction = list(best_path.keys())
most_moves = best_path[best_direction[0]]

print(best_direction[0])
print(*most_moves, sep="\n")
print(total_eggs)
