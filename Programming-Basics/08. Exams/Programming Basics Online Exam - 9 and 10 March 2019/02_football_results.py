first_game_result = input()
second_game_result = input()
third_game_result = input()
won_games = 0
lost_games = 0
drawn_games = 0

if first_game_result[0] > first_game_result[2]:
    won_games += 1
elif first_game_result[0] < first_game_result[2]:
    lost_games += 1
else:
    drawn_games += 1

if second_game_result[0] > second_game_result[2]:
    won_games += 1
elif second_game_result[0] < second_game_result[2]:
    lost_games += 1
else:
    drawn_games += 1

if third_game_result[0] > third_game_result[2]:
    won_games += 1
elif third_game_result[0] < third_game_result[2]:
    lost_games += 1
else:
    drawn_games += 1

print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {drawn_games}")
