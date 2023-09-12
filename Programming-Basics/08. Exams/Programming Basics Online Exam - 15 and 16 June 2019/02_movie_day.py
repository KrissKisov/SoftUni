time_shooting = int(input())
num_scene = int(input())
time_per_scene = int(input())
preparation = time_shooting * 0.15

time_needed = num_scene * time_per_scene + preparation

time_difference = round(time_shooting - time_needed)

if time_difference >= 0:
    print(f"You managed to finish the movie on time! You have {time_difference} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {abs(time_difference)} minutes.")
