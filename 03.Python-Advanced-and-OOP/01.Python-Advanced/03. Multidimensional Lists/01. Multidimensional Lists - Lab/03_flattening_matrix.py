rows = int(input())

flatten_matrix = []

for _ in range(rows):
    flatten_matrix.extend(int(x) for x in input().split(', '))

print(flatten_matrix)

# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])
#
# # flatten_matrix = []
# # for row in matrix:
# #     for num in row:
# #         flatten_matrix.append(num)
#
# flatten_matrix = [num for row in matrix for num in row]
#
# print(flatten_matrix)
