def students_credits(*args):

    diyan_progres = {}

    for info in args:
        course_name, course_credits, max_test_points, diyan_points = info.split("-")
        course_credits, max_test_points, diyan_points = int(course_credits), int(max_test_points), int(diyan_points)

        percentage = diyan_points / max_test_points
        achieved_credits = course_credits * percentage

        diyan_progres[course_name] = achieved_credits

    diyan_progres = dict(sorted(diyan_progres.items(), key=lambda kvp: -kvp[-1]))

    message = ""
    total_credits = sum(diyan_progres.values())

    if total_credits >= 240:
        message += f"Diyan gets a diploma with {total_credits :.1f} credits.\n"
    else:
        needed_credits = 240 - total_credits
        message += f"Diyan needs {needed_credits :.1f} credits more for a diploma.\n"

    message += '\n'.join(f"{key} - {value :.1f}" for key, value in diyan_progres.items())

    return message


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
