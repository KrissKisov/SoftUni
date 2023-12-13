command = input()
best_scorer = ""
best_player_goals = 0
is_hat_trick = False
while command != "END":
    player_name = command
    goal_scored = int(input())
    if goal_scored > best_player_goals:
        best_scorer = player_name
        best_player_goals = goal_scored

    if goal_scored >= 10:
        is_hat_trick = True
        break
    elif goal_scored >= 3:
        is_hat_trick = True

    command = input()
if is_hat_trick:
    print(f"{best_scorer} is the best player!")
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_scorer} is the best player!")
    print(f"He has scored {best_player_goals} goals.")
