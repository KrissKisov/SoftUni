from math import ceil


number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
student_attendances = 0

for student in range(number_of_the_students):
    current_student_attendances = int(input())
    total_bonus = current_student_attendances / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        student_attendances = current_student_attendances

print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {student_attendances} lectures.")
