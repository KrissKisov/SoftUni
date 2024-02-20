command = input()

most_points_player = ""
points = 0

while command != "Stop":
    player_name = command

    current_player_points = 0
    for letter in player_name:
        number = int(input())

        if number == ord(letter):
            current_player_points += 10
        else:
            current_player_points += 2

        if current_player_points >= points:
            points = current_player_points
            most_points_player = player_name

    command = input()

print(f"The winner is {most_points_player} with {points} points!")
