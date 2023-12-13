actor_name = input()
starting_points = float(input())
judges_count = int(input())

points_needed = 1250.5
actor_points = starting_points
for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    actor_points += len(judge_name) * judge_points / 2
    if actor_points > points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points :.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {points_needed - actor_points :.1f} more!")
