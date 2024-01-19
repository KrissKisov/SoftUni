rows, columns = (int(x) for x in input().split(', '))

matrix = []
sum_of_matrix = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    sum_of_matrix += sum(matrix[row])

print(sum_of_matrix)
print(matrix)
