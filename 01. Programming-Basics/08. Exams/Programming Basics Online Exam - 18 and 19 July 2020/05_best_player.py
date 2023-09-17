command = input()
top_player = ""
most_scored_goals = 0
is_hat_trick = False
while command != "END":
    current_player = command
    scored_goals = int(input())

    if scored_goals > most_scored_goals:
        most_scored_goals = scored_goals
        top_player = current_player

    if scored_goals >= 3:
        is_hat_trick = True

    if scored_goals >= 10:
        break

    command = input()

print(f"{top_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {most_scored_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_scored_goals} goals.")
