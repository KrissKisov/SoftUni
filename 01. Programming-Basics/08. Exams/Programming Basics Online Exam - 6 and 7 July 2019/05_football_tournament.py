football_team = input()
played_games = int(input())
won_games = 0
drew_games = 0
lost_games = 0
points = 0
for game in range(played_games):
    result = input()

    if result == "W":
        won_games += 1
        points += 3

    elif result == "D":
        drew_games += 1
        points += 1

    else:
        lost_games += 1

if played_games <= 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    percent_wins = won_games / played_games * 100
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {won_games}")
    print(f"## D: {drew_games}")
    print(f"## L: {lost_games}")
    print(f"Win rate: {percent_wins :.2f}%")
