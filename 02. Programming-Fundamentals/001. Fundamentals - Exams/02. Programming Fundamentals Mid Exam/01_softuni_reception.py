receptionist_one_efficiency = int(input())
receptionist_two_efficiency = int(input())
receptionist_three_efficiency = int(input())
number_of_students = int(input())
total_per_hour = receptionist_one_efficiency + receptionist_two_efficiency + receptionist_three_efficiency
hours = 0
while number_of_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    number_of_students -= total_per_hour
    if number_of_students <= 0:
        break

print(f"Time needed: {hours}h.")
