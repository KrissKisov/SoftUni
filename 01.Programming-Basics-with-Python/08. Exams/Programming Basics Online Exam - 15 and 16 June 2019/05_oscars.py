actor = input()
academy_points = float(input())
num_appraisers = int(input())

actor_points = academy_points
for _ in range(num_appraisers):
    appraiser_name = input()
    appraiser_points = float(input())
    actor_points += (len(appraiser_name) * appraiser_points / 2)

    if actor_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {actor_points :.1f}!")
        break
else:
    points_needed = 1250.5 - actor_points
    print(f"Sorry, {actor} you need {points_needed :.1f} more!")
