board_size = int(input())

board = []
gambler_pos = None
money = 100
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(board_size):
    board.append([x for x in input()])

    if "G" in board[row]:
        gambler_pos = [row, board[row].index("G")]

command = input()

while command != "end":

    r, c = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if r not in range(board_size) and c not in range(board_size):
        money = 0
        print("Game over! You lost everything!")
        break

    elif board[r][c] == "-":
        board[gambler_pos[0]][gambler_pos[1]] = "-"
        board[r][c] = "G"
        gambler_pos = [r, c]

    elif board[r][c] == "W":
        board[gambler_pos[0]][gambler_pos[1]] = "-"
        gambler_pos = [r, c]
        board[r][c] = "G"
        money += 100

    elif board[r][c] == "P":
        board[gambler_pos[0]][gambler_pos[1]] = "-"
        gambler_pos = [r, c]
        board[r][c] = "G"
        money -= 200

        if money <= 0:
            print("Game over! You lost everything!")
            break

    elif board[r][c] == "J":
        board[gambler_pos[0]][gambler_pos[1]] = "-"
        gambler_pos = [r, c]
        board[r][c] = "G"
        money += 100000
        print("You win the Jackpot!")
        break

    command = input()

if money > 0:
    print(f"End of the game. Total amount: {money}$")
    [print(*row, sep="") for row in board]
