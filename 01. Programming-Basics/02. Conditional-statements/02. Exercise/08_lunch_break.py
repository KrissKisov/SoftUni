from math import ceil

film = input()
episode_duration = int(input())
break_duration = int(input())

time_to_eat = break_duration / 8
time_to_rest = break_duration / 4
time_for_watching = break_duration - (time_to_eat + time_to_rest)

if episode_duration <= time_for_watching:
    print(f"You have enough time to watch {film} and left with {ceil(time_for_watching - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {film}, you need {ceil(episode_duration - time_for_watching)} more minutes.")
