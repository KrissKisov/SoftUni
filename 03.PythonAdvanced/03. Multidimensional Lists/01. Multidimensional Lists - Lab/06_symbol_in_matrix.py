##1

# num = int(input())
#
# matrix = [[x for x in input()] for _ in range(num)]
#
# symbol = input()
#
# symbol_found = False
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         current_symbol = matrix[row_index][col_index]
#         if current_symbol == symbol:
#             print(f"({row_index}, {col_index})")
#             symbol_found = True
#             break
#     if symbol_found:
#         break
# if not symbol_found:
#     print(f"{symbol} does not occur in the matrix")

##2

num = int(input())

matrix = [[x for x in input()] for _ in range(num)]

symbol = input()


for index, row in enumerate(matrix):
    if symbol in row:
        print(f"({index}, {row.index(symbol)})")
        break
else:
    print(f"{symbol} does not occur in the matrix")
