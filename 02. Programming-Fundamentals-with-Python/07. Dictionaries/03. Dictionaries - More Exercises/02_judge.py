contests_dictionary = {}
users = {}
command = input().split(" -> ")
while command[0] != "no more time":
    username, contest, points = command[0], command[1], int(command[2])
    if contest not in contests_dictionary.keys():
        contests_dictionary[contest] = {}

    if username not in contests_dictionary[contest].keys():
        contests_dictionary[contest][username] = points
    else:
        if contests_dictionary[contest][username] < points:
            contests_dictionary[contest][username] = points

    if username not in users.keys():
        users[username] = {}

    if contest not in users[username].keys():
        users[username][contest] = points
    else:
        if users[username][contest] < points:
            users[username][contest] = points

    command = input().split(" -> ")

for subject, info in contests_dictionary.items():
    # contests_dictionary[subject] = dict(sorted(info.items(), key=lambda x: x[-1], reverse=True))
    contests_dictionary[subject] = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    print(f"{subject}: {len(contests_dictionary[subject].keys())} participants")
    number = 0
    for user, user_points in contests_dictionary[subject].items():
        number += 1
        print(f"{number}. {user} <::> {user_points}")

for user, user_info in users.items():
    for key, value in user_info.items():
        users[user] = sum(user_info.values())

# users = dict(sorted(users.items(), key=lambda x: x[-1], reverse=True))
users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
number = 0
print("Individual standings:")
for user in users.keys():
    number += 1
    print(f"{number}. {user} -> {users[user]}")

'''
 # users = dict(sorted(users.items(), key=lambda x: x[-1], reverse=True)) -> this sorts the dictionary by value in
 descending order but if there are two keys with same value they will be ordered by order of input.
 # users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0]))) -> this again sortd the dictionary by value in
 in descending order but if two keys have same value they'll be sorted ascending.
'''