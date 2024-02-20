from math import floor

tournaments = int(input())
starting_points = int(input())

winner_points = 2000
finalist_points = 1200
semi_finalist_points = 720
total_points = starting_points
won_tournaments = 0
for num in range(tournaments):
    achievement = input()  # "W", "F" или "SF"
    if achievement == "W":
        won_tournaments += 1
        total_points += winner_points
    elif achievement == "F":
        total_points += finalist_points
    elif achievement == "SF":
        total_points += semi_finalist_points

average_points = (total_points - starting_points) / tournaments
percent_wins = won_tournaments / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_wins :.2f}%")
