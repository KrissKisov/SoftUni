rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sub_matrix_sum = float('-inf')
sub_matrix_nums = []
for row in range(rows - 1):
    for col in range(columns - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]
        current_sum = top_left + top_right + bottom_left + bottom_right

        if current_sum > max_sub_matrix_sum:
            max_sub_matrix_sum = current_sum
            sub_matrix = [[top_left, top_right], [bottom_left, bottom_right]]
            sub_matrix_nums = sub_matrix

print(*sub_matrix_nums[0])
print(*sub_matrix_nums[1])
print(max_sub_matrix_sum)
