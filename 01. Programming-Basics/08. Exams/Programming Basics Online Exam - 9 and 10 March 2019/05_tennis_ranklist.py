number_of_tournaments = int(input())
start_points = int(input())
won_tournaments = 0
won_points = 0

for tournament in range(number_of_tournaments):
    reached_stage = input()  # "W", "F" или "SF"
    current_points = 0

    if reached_stage == "W":
        won_tournaments += 1
        current_points += 2000
    elif reached_stage == "F":
        current_points += 1200
    else:  # reached_stage == "SF"
        current_points += 720

    won_points += current_points
    start_points += current_points

average_won_points = won_points // number_of_tournaments
percent_won_tournaments = won_tournaments / number_of_tournaments * 100

print(f"Final points: {start_points}")
print(f"Average points: {average_won_points}")
print(f"{percent_won_tournaments :.2f}%")
