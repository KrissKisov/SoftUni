students = int(input())

top_students = 0
good_students = 0
average_students = 0
fail_students = 0
accumulated_grade = 0
for each_student in range(students):
    grade = float(input())
    accumulated_grade += grade
    if grade >= 5:
        top_students +=1
    elif grade >= 4:
        good_students += 1
    elif grade >= 3:
        average_students += 1
    elif grade >= 2:
        fail_students += 1

top_students_percent = top_students / students * 100
good_students_percent = good_students / students * 100
average_students_percent = average_students / students * 100
fail_students_percent = fail_students / students * 100
average_grade = accumulated_grade / students
print(f"Top students: {top_students_percent :.2f}%")
print(f"Between 4.00 and 4.99: {good_students_percent :.2f}%")
print(f"Between 3.00 and 3.99: {average_students_percent :.2f}%")
print(f"Fail: {fail_students_percent :.2f}%")
print(f"Average: {average_grade :.2f}")
