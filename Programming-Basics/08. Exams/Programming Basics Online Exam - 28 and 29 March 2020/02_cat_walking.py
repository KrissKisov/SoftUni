minutes_walk = int(input())
number_of_walks = int(input())
intake_calories = int(input())

total_minutes_walked = minutes_walk * number_of_walks
burnt_calories = total_minutes_walked * 5

if burnt_calories >= intake_calories * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")
