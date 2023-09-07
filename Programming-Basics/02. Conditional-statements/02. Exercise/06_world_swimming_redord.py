from math import floor

world_record_time = float(input())
distance = float(input())
time_per_meter = float(input())

distance_for_delay = floor(distance / 15)
delay_time = distance_for_delay * 12.5

current_time = distance * time_per_meter
current_time += delay_time

if current_time < world_record_time:
    print(f"Yes, he succeeded! The new world record is {current_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {current_time - world_record_time:.2f} seconds slower.")
