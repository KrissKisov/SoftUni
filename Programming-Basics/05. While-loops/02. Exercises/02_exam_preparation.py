failed_grades_allowance = int(input())

total_grades = 0
exercises_count = 0
bad_grades_count = 0
total_fails = 0
last_exercise = ""
while total_fails < failed_grades_allowance:
    exercise_name = input()
    if exercise_name == "Enough":
        break
    exercise_grade = input()
    if exercise_grade <= "4":
        bad_grades_count += 1
        if bad_grades_count >= failed_grades_allowance:
            break
    exercises_count += 1
    current_grade = int(exercise_grade)
    total_grades += current_grade
    last_exercise = exercise_name

average_grades = total_grades / exercises_count
if bad_grades_count >= failed_grades_allowance:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {exercises_count}")
    print(f"Last problem: {last_exercise}")

