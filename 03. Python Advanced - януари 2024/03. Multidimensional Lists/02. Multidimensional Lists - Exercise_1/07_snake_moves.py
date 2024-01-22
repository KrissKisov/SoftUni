from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(input())

matrix = []

for row in range(rows):
    row_data = []
    if row % 2 == 0:
        for col in range(columns):
            letter = snake.popleft()
            row_data.append(letter)
            snake.append(letter)
        matrix.append(row_data)
    else:
        for col in range(columns - 1, -1, -1):
            letter = snake.popleft()
            row_data.append(letter)
            snake.append(letter)
        matrix.append(row_data[::-1])

for current_row in matrix:
    print(*current_row, sep="")
