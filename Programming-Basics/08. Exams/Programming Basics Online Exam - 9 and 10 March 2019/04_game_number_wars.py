first_player_name = input()
second_player_name = input()
points_first_player = 0
points_second_player = 0
is_number_wars = False

while True:
    command = input()
    if command == "End of game":
        break

    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        points_first_player += first_player_card - second_player_card

    elif first_player_card < second_player_card:
        points_second_player += second_player_card - first_player_card

    else:
        is_number_wars = True
        break

if is_number_wars:
    print("Number wars!")
    first_player_card = int(input())
    second_player_card = int(input())

    if first_player_card > second_player_card:
        print(f"{first_player_name} is winner with {points_first_player} points")
    elif second_player_card > first_player_card:
        print(f"{second_player_name} is winner with {points_second_player} points")

else:
    print(f"{first_player_name} has {points_first_player} points")
    print(f"{second_player_name} has {points_second_player} points")
