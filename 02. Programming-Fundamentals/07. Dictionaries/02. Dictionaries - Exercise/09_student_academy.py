number = int(input())
students_grades = {}

for i in range(number):
    student = input()
    grade = float(input())
    if student not in students_grades.keys():
        students_grades[student] = []
    students_grades[student].append(grade)

to_remove = []
for student in students_grades.keys():
    average_grade = sum(students_grades[student]) / len(students_grades[student])
    if average_grade < 4.50:
        to_remove.append(student)

for student in to_remove:
    del students_grades[student]

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {average_grade :.2f}")
