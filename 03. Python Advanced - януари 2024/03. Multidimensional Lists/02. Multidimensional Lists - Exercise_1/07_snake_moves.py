from collections import deque

rows, columns = [int(x) for x in input().split()]
word = deque(input())

for row in range(rows):
    row_data = []
    if row % 2 == 0:
        for col in range(columns):
            letter = word.popleft()
            row_data.append(letter)
            word.append(letter)
        print(*row_data, sep="")
    else:
        for col in range(columns - 1, -1, -1):
            letter = word.popleft()
            row_data.append(letter)
            word.append(letter)
        print(*row_data[::-1], sep="")
