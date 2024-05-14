size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

coordinates = [[int(x) for x in line.split(',')] for line in input().split()]

cells = (
    (-1, -1),  # "top_left"
    (-1, 0),  # top_middle
    (-1, 1),  # top_right
    (0, -1),  # "middle_left"
    (0, 1),  # "middle_right"
    (1, -1),  # "bottom_left"
    (1, 0),  # "bottom_middle"
    (1, 1),  # "bottom_right"
    (0, 0)  # "bomb"
)

for position in coordinates:
    row, col = position

    if matrix[row][col] < 0:
        continue

    for cell in cells:
        bomb_radius_row = row + cell[0]
        bomb_radius_col = col + cell[1]
        if bomb_radius_row in range(size) and bomb_radius_col in range(size):
            matrix[row + cell[0]][col + cell[1]] -= matrix[row][col] if matrix[row + cell[0]][col + cell[1]] > 0 else 0

alive_cells = [num for row in range(size) for num in matrix[row] if num > 0]
# alive_ cells = 0
# final_sum = 0
# for row in matrix:
#     for num in row:
#         if num > 0:
#             alive_cells += 1
#             final_sum += num

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
