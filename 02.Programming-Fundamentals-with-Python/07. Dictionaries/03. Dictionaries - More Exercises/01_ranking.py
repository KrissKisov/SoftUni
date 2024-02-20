contest_password_dictionary = {}
first_input_line = input().split(":")
while len(first_input_line) > 1:
    contest = first_input_line[0]
    password_for_contest = first_input_line[1]
    contest_password_dictionary[contest] = password_for_contest

    first_input_line = input().split(":")

users_dictionary = {}
second_input_line = input()
while second_input_line != "end of submissions":
    contest_to_check, password, username, points = second_input_line.split("=>")
    points = int(points)
    for contest, password_for_contest in contest_password_dictionary.items():
        if contest_to_check == contest and password == password_for_contest:
            if username not in users_dictionary.keys():
                users_dictionary[username] = {}
            if contest not in users_dictionary[username].keys():
                users_dictionary[username][contest] = points
            if points > users_dictionary[username][contest]:
                users_dictionary[username][contest] = points

    second_input_line = input()

total_points_dictionary = {}
for user in users_dictionary.keys():
    total_points_dictionary[user] = 0
    for contest, points in users_dictionary[user].items():
        total_points_dictionary[user] += points

max_points = max(total_points_dictionary.values())
user_with_max_points = {user: points for user, points in total_points_dictionary.items() if points == max_points}
for user, points in user_with_max_points.items():
    print(f"Best candidate is {user} with total {points} points.")
print("Ranking:")
users_dictionary = dict(sorted(users_dictionary.items()))
for user in users_dictionary.keys():
    users_dictionary[user] = dict(sorted(users_dictionary[user].items(), key=lambda x: x[1], reverse=True))

for user in users_dictionary.keys():
    print(user)
    for contest, points in users_dictionary[user].items():
        print(f"#  {contest} -> {points}")
