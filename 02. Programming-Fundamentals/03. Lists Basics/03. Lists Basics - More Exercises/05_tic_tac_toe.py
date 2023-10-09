first_line = input().split()
second_line = input().split()
third_line = input().split()
game_field = [first_line, second_line, third_line]

winner = ""

if game_field[0][0] == "1" and game_field[0][1] == "1" and game_field[0][2] == "1":
    winner = "first_player"
elif game_field[1][0] == "1" and game_field[1][1] == "1" and game_field[1][2] == "1":
    winner = "first_player"
elif game_field[2][0] == "1" and game_field[2][1] == "1" and game_field[2][2] == "1":
    winner = "first_player"
elif game_field[0][0] == "1" and game_field[1][0] == "1" and game_field[2][0] == "1":
    winner = "first_player"
elif game_field[0][1] == "1" and game_field[1][1] == "1" and game_field[2][1] == "1":
    winner = "first_player"
elif game_field[0][2] == "1" and game_field[1][2] == "1" and game_field[2][2] == "1":
    winner = "first_player"
elif game_field[0][0] == "1" and game_field[1][1] == "1" and game_field[2][2] == "1":
    winner = "first_player"
elif game_field[0][2] == "1" and game_field[1][1] == "1" and game_field[2][0] == "1":
    winner = "first_player"
elif game_field[0][0] == "2" and game_field[0][1] == "2" and game_field[0][2] == "2":
    winner = "second_player"
elif game_field[1][0] == "2" and game_field[1][1] == "2" and game_field[1][2] == "2":
    winner = "second_player"
elif game_field[2][0] == "2" and game_field[2][1] == "2" and game_field[2][2] == "2":
    winner = "second_player"
elif game_field[0][0] == "2" and game_field[1][0] == "2" and game_field[2][0] == "2":
    winner = "second_player"
elif game_field[0][1] == "2" and game_field[1][1] == "2" and game_field[2][1] == "2":
    winner = "second_player"
elif game_field[0][2] == "2" and game_field[1][2] == "2" and game_field[2][2] == "2":
    winner = "second_player"
elif game_field[0][0] == "2" and game_field[1][1] == "2" and game_field[2][2] == "2":
    winner = "second_player"
elif game_field[0][2] == "2" and game_field[1][1] == "2" and game_field[2][0] == "2":
    winner = "second_player"

if winner == "first_player":
    print("First player won")
elif winner == "second_player":
    print("Second player won")
else:
    print("Draw!")
