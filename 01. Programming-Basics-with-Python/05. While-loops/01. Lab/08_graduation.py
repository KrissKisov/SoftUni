student_name = input()
year_count = 1
total_grade = 0
fails = 0
while year_count <= 12:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            break
        continue
    year_count += 1
    total_grade += grade

if year_count <= 12:
    print(f"{student_name} has been excluded at {year_count} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
