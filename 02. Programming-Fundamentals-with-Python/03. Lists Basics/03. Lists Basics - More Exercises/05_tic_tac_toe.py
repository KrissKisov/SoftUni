first_line = input().split()
second_line = input().split()
third_line = input().split()
game_field = [first_line, second_line, third_line]

winner = ""

if game_field[0][0] == "1" and game_field[0][1] == "1" and game_field[0][2] == "1":
    winner = "First player won"
elif game_field[1][0] == "1" and game_field[1][1] == "1" and game_field[1][2] == "1":
    winner = "First player won"
elif game_field[2][0] == "1" and game_field[2][1] == "1" and game_field[2][2] == "1":
    winner = "First player won"
elif game_field[0][0] == "1" and game_field[1][0] == "1" and game_field[2][0] == "1":
    winner = "First player won"
elif game_field[0][1] == "1" and game_field[1][1] == "1" and game_field[2][1] == "1":
    winner = "First player won"
elif game_field[0][2] == "1" and game_field[1][2] == "1" and game_field[2][2] == "1":
    winner = "First player won"
elif game_field[0][0] == "1" and game_field[1][1] == "1" and game_field[2][2] == "1":
    winner = "First player won"
elif game_field[0][2] == "1" and game_field[1][1] == "1" and game_field[2][0] == "1":
    winner = "First player won"
elif game_field[0][0] == "2" and game_field[0][1] == "2" and game_field[0][2] == "2":
    winner = "Second player won"
elif game_field[1][0] == "2" and game_field[1][1] == "2" and game_field[1][2] == "2":
    winner = "Second player won"
elif game_field[2][0] == "2" and game_field[2][1] == "2" and game_field[2][2] == "2":
    winner = "Second player won"
elif game_field[0][0] == "2" and game_field[1][0] == "2" and game_field[2][0] == "2":
    winner = "Second player won"
elif game_field[0][1] == "2" and game_field[1][1] == "2" and game_field[2][1] == "2":
    winner = "Second player won"
elif game_field[0][2] == "2" and game_field[1][2] == "2" and game_field[2][2] == "2":
    winner = "Second player won"
elif game_field[0][0] == "2" and game_field[1][1] == "2" and game_field[2][2] == "2":
    winner = "Second player won"
elif game_field[0][2] == "2" and game_field[1][1] == "2" and game_field[2][0] == "2":
    winner = "Second player won"
else:
    winner = "Draw!"

print(winner)
