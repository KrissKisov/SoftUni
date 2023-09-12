series = input()
num_seasons = int(input())
num_episodes = int(input())
episode_duration = float(input())
ads = episode_duration * 0.2
special_episode_addition = 10

total_time_episode = episode_duration + ads
total_time_season = num_episodes * total_time_episode + 10
total_time_series = int(num_seasons * total_time_season)

print(f"Total time needed to watch the {series} series is {total_time_series} minutes.")
