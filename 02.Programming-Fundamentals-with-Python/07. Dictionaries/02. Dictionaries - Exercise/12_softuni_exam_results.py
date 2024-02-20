students_result = {}
language_submissions = {}
command = input()
while command != "exam finished":
    current_command = command.split("-")
    username = current_command[0]
    if "banned" in command:
        del students_result[username]

    else:
        language = current_command[1]
        points = int(current_command[2])
        if username not in students_result.keys():
            students_result[username] = points

        if points > students_result[username]:
            students_result[username] = points

        if language not in language_submissions.keys():
            language_submissions[language] = 0
        language_submissions[language] += 1

    command = input()
print("Results:")
for username, points in students_result.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions in language_submissions.items():
    print(f"{language} - {submissions}")
