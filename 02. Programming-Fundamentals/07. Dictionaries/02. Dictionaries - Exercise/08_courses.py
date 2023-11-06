courses = {}
command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
