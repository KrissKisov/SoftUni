current_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delay = int(distance / 50) * 30
final_time = total_time + delay

if final_time < current_record:
    print(f"Yes! The new record is {final_time :.2f} seconds.")
else:
    print(f"No! He was {final_time - current_record :.2f} seconds slower.")
