# def gather_credits(needed_credits, *course_info):
#     total_credits = 0
#     courses = set()
#
#     while total_credits < needed_credits:
#
#         for course_name, current_credits in course_info:
#
#             if course_name not in courses:
#                 courses.add(course_name)
#                 total_credits += current_credits
#
#             if total_credits >= needed_credits:
#                 break
#
#         else:
#             break
#
#     if total_credits < needed_credits:
#         credits_shortage = needed_credits - total_credits
#         return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
#
#     return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(courses))}"

def gather_credits(needed_credits, *course_info):
    total_credits = 0
    courses = set()

    for course_name, current_credits in course_info:

        if total_credits >= needed_credits:
            break

        if course_name not in courses:
            courses.add(course_name)
            total_credits += current_credits

    if total_credits < needed_credits:
        credits_shortage = needed_credits - total_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

    return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(courses))}"


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

# # outputs
# You need to enroll in more courses! You have to gather 53 credits more.
#
# Enrollment finished! Maximum credits: 84.
# Courses: Advanced, Basics, Fundamentals
#
# Enrollment finished! Maximum credits: 84.
# Courses: Advanced, Basics, Fundamentals
