from math import floor

hours_needed = int(input())
days_for_project = int(input())
employees_count = int(input())

remaining_days = days_for_project * 0.90
hours_per_day = 8
over_time = 2
total_hours_per_day = hours_per_day + over_time
total_work_hours = floor(total_hours_per_day * remaining_days * employees_count)

if total_work_hours >= hours_needed:
    print(f"Yes!{total_work_hours - hours_needed} hours left.")
else:
    print(f"Not enough time!{hours_needed - total_work_hours} hours needed.")
