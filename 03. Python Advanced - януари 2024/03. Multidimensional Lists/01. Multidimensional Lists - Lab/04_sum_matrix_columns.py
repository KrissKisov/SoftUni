rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for col in range(columns):
    column_sum = 0
    for row in range(len(matrix)):
        column_sum += matrix[row][col]

    print(column_sum)
