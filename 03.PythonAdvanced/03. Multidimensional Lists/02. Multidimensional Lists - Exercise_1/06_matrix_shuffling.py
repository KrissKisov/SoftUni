rows, columns = [int(x) for x in input().split()]

# matrix = [[x for x in input().split()] for _ in range(rows)]
matrix = [input().split() for _ in range(rows)]

command = input().split()

while command[0] != "END":
    current_command, *nums = command
    if "swap" == current_command and len(nums) == 4:
        row_1, col_1, row_2, col_2 = list(int(x) for x in nums)

        if row_1 in range(rows) and row_2 in range(rows) and col_1 in range(columns) and col_2 in range(columns):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            [print(*row) for row in matrix]

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

    command = input().split()
