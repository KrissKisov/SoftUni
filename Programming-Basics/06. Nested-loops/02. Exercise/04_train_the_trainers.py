number_of_judges = int(input())
presentation_count = 0
average_all_presentations = 0

command = input()
while command != "Finish":
    presentation = command
    total_grade = 0

    for grade in range(number_of_judges):
        current_grade = float(input())
        total_grade += current_grade

    presentation_count += 1
    average_grade_presentation = total_grade / number_of_judges
    average_all_presentations += average_grade_presentation
    print(f"{presentation} - {average_grade_presentation :.2f}.")

    command = input()

print(f"Student's final assessment is {average_all_presentations / presentation_count :.2f}.")
