courses = {}

while True:
    input_line = input()
    if ":" not in input_line:
        searched_in_course = input_line.replace("_", " ")
        # searched_in_course = " ".join(input_line.split("_"))
        break
    name, ID, course = input_line.split(":")
    if course not in courses:
        courses[course] = {ID: name}
    courses[course][ID] = name

if searched_in_course in courses:
    for ID, name in courses[searched_in_course].items():
        print(f"{name} - {ID}")
