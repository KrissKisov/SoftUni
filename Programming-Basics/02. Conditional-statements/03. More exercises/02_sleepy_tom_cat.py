count_days_off = int(input())

minutes_to_play_yearly = 30000
work_day_play = 63
day_off_play = 127

play_time = count_days_off * day_off_play + (365 - count_days_off) * 63
difference = abs(minutes_to_play_yearly - play_time)
hours_play_time = difference // 60
minutes_play_time = difference % 60

if play_time > minutes_to_play_yearly:
    print("Tom will run away")
    print(f"{hours_play_time} hours and {minutes_play_time} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_play_time} hours and {minutes_play_time} minutes less for play")
