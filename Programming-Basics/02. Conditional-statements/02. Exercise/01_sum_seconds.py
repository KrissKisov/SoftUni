first_time_in_seconds = int(input())
second_time_in_seconds = int(input())
third_time_in_seconds = int(input())

total_time = first_time_in_seconds + second_time_in_seconds + third_time_in_seconds
minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
