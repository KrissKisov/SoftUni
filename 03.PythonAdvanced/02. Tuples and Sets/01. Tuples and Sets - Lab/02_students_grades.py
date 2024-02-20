number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    student, grade = input().split()
    grade = float(grade)

    if student not in students.keys():
        students[student] = []
    students[student].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    grades = [f"{grade :.2f}" for grade in grades]
    print(f"{name} ->", *grades, f"(avg: {average_grade :.2f})")
