def softuni_students(*student_info, **course_info):
    valid_students = {}
    invalid_students = []
    result = []

    for info in student_info:
        if info[0] in course_info.keys():
            valid_students[info[1]] = info[0]

        else:
            invalid_students.append(info[1])

    if valid_students:
        valid_students = dict(sorted(valid_students.items(), key=lambda x: x[0]))

    if invalid_students:
        invalid_students = sorted(invalid_students)

    for name, info in valid_students.items():
        course_name = course_info[info]
        result.append(f"*** A student with the username {name} has successfully finished the course {course_name}!")

    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(invalid_students)}")

    return '\n'.join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
# *** A student with the username Kaloyan9905 has successfully finished the course Python Web Framework!


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
# *** A student with the username Silvester1 has successfully finished the course Spring Advanced!
# *** A student with the username The programmer has successfully finished the course Spring Advanced!
# !!! Invalid course students: Katq21


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
# *** A student with the username Bobosa253 has successfully finished the course HTML & CSS!
# *** A student with the username KrasimirAtanasov has successfully finished the course JS Advanced!
# *** A student with the username Programmingkitten has successfully finished the course Machine Learning!
# !!! Invalid course students: DaniBG, MitkoTheDark
