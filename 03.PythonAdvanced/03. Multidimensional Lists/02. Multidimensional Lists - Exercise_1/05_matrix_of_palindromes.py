rows, columns = [int(x) for x in input().split()]

start = ord('a')

matrix = []

for row in range(rows):
    row_data = []
    for col in range(columns):
        palindrome = chr(start + row) + chr(start + row + col) + chr(start + row)
        row_data.append(palindrome)

    matrix.append(row_data)

for row in matrix:
    print(*row, sep=" ", end=" ")
    print()

#
# rows, cols = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(chr(row), chr(col), chr(row), sep="", end=" ")
#
#     print()
