control_time_minutes = int(input())
control_time_seconds = int(input())
track_length = float(input())
seconds_per_100m = int(input())
time_to_be_improved = control_time_minutes * 60 + control_time_seconds
current_time = track_length / 100 * seconds_per_100m - track_length / 120 * 2.5

if current_time <= time_to_be_improved:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {current_time :.3f}.")
else:
    difference = current_time - time_to_be_improved
    print(f"No, Marin failed! He was {difference :.3f} second slower.")
