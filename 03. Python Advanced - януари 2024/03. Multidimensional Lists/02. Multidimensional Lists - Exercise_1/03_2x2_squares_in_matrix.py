rows, columns = (int(x) for x in input().split())

matrix = [input().split() for _ in range(rows)]
square_matrices = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]

        if top_left == top_right == bottom_left == bottom_right:
            square_matrices += 1

print(square_matrices)
