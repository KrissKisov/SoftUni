# # solution_1
#
# player_name = input()
# command = input()
# start_points = 301
# successful_shots_count = 0
# unsuccessful_shots_count = 0
#
# while command != "Retire":
#     sector = command
#     points = int(input())
#
#     if sector == "Double":
#         points *= 2
#     elif sector == "Triple":
#         points *= 3
#
#     if start_points >= points:
#         successful_shots_count += 1
#         start_points -= points
#     else:
#         unsuccessful_shots_count += 1
#         command = input()
#         continue
#
#     if start_points == 0:
#         break
#
#     command = input()
#
# if start_points == 0:
#     print(f"{player_name} won the leg with {successful_shots_count} shots.")
# else:
#     print(f"{player_name} retired after {unsuccessful_shots_count} unsuccessful shots.")
#
# # solution_2

player_name = input()
start_points = 301
successful_shots_count = 0
unsuccessful_shots_count = 0

while start_points != 0:
    sector = input()
    if sector == "Retire":
        break

    points = int(input())

    if sector == "Double":
        points *= 2
    elif sector == "Triple":
        points *= 3

    if start_points >= points:
        successful_shots_count += 1
        start_points -= points
    else:
        unsuccessful_shots_count += 1
        continue

if start_points == 0:
    print(f"{player_name} won the leg with {successful_shots_count} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots_count} unsuccessful shots.")
