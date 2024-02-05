size = int(input())

matrix = []

# knight_moves = [(x, y) for x in [-1, 1, -2, 2] for y in [-1, 1, -2, 2] if abs(x) != abs(y)]
knight_moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)

knights = []

for row in range(size):
    current_row = list(input())
    matrix.append(current_row)

    if "K" in current_row:
        knights.extend([(row, i) for i, x in enumerate(current_row) if x == "K"])

knights_to_remove = 0

while knights:
    max_attacks = 0
    knight_max_attacks = []

    for knight in knights:
        current_num_attacks = 0
        for move in knight_moves:
            r, c = knight[0] + move[0], knight[1] + move[1]

            if r in range(size) and c in range(size):
                if matrix[r][c] == "K":
                    current_num_attacks += 1

        if current_num_attacks > max_attacks:
            max_attacks = current_num_attacks
            knight_max_attacks = knight

    if not knight_max_attacks:
        break

    matrix[knight_max_attacks[0]][knight_max_attacks[1]] = "0"
    knights_to_remove += 1
    knights.remove(knight_max_attacks)

print(knights_to_remove)
