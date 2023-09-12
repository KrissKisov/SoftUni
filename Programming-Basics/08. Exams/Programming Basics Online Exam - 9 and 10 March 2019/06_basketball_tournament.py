command = input()
won_games = 0
lost_games = 0
played_games = 0

while command != "End of tournaments":
    tournament = command

    num_games = int(input())
    for game in range(1, num_games + 1):
        played_games += 1
        scored_points = int(input())
        received_points = int(input())

        difference = scored_points - received_points
        if difference > 0:
            won_games += 1
            print(f"Game {game} of tournament {tournament}: win with {difference} points.")
        elif difference < 0:
            lost_games += 1
            print(f"Game {game} of tournament {tournament}: lost with {abs(difference)} points.")

    command = input()

percent_won_games = won_games / played_games * 100
percent_lost_games = lost_games / played_games * 100
print(f"{percent_won_games :.2f}% matches win")
print(f"{percent_lost_games :.2f}% matches lost")
