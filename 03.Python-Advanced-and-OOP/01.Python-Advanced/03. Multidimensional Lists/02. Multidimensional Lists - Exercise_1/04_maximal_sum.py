##1
#
# rows, columns = [int(x) for x in input().split()]
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# max_sum = float('-inf')
# max_sub_matrix = tuple()
#
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         top_left = matrix[row][col]
#         top_middle = matrix[row][col + 1]
#         top_right = matrix[row][col + 2]
#         middle_left = matrix[row + 1][col]
#         centre = matrix[row + 1][col + 1]
#         middle_right = matrix[row + 1][col + 2]
#         bottom_left = matrix[row + 2][col]
#         bottom_middle = matrix[row + 2][col + 1]
#         bottom_right = matrix[row + 2][col + 2]
#
#         current_matrix_elements = (
#             top_left, top_middle, top_right, middle_left, centre, middle_right, bottom_left, bottom_middle, bottom_right
#         )
#         if sum(current_matrix_elements) > max_sum:
#             max_sum = sum(current_matrix_elements)
#             max_sub_matrix = current_matrix_elements
#
# print(f"Sum = {max_sum}")
# for i in range(0, len(max_sub_matrix), 3):
#     print(*max_sub_matrix[i:i + 3])

##2

rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_sub_matrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        if sum(matrix[row][col:col+3]) + sum(matrix[row+1][col:col+3]) + sum(matrix[row+2][col:col+3]) > max_sum:
            max_sum = sum(matrix[row][col:col+3]) + sum(matrix[row+1][col:col+3]) + sum(matrix[row+2][col:col+3])
            max_sub_matrix = [matrix[row][col:col+3], matrix[row+1][col:col+3], matrix[row+2][col:col+3]]

print(f"Sum = {max_sum}")
for i in range(len(max_sub_matrix)):
    print(*max_sub_matrix[i])
