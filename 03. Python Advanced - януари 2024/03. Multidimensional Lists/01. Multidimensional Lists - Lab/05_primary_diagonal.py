number = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(number)]

diagonal_sum = 0

for index in range(len(matrix)):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)
