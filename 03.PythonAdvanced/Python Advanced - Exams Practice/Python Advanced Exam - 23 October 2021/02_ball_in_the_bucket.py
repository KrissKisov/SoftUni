def calculate_points(col, matrix):
    point = 0

    for col in range(col, col + 1):
        for row in range(len(matrix)):
            point += matrix[row][col] if isinstance(matrix[row][col], int) else 0

    return point


rows, columns = 6, 6

board = []
total_points = 0
for i in range(6):
    board.append([int(x) if x.isdigit() else str(x) for x in input().split()])

for throw in range(3):
    r, c = [int(x) for x in input()[1:-1].split(", ")]

    if r in range(rows) and c in range(columns):

        if board[r][c] == "B":
            board[r][c] = 0
            total_points += calculate_points(c, board)

prize = ""

if 100 <= total_points <= 199:
    prize += "Football"
elif 200 <= total_points <= 299:
    prize += "Teddy Bear"
elif total_points >= 300:
    prize += "Lego Construction Set"

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    needed_points = 100 - total_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
