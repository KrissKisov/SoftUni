from math import inf

command = input()

min_number = float(inf)
while command != "Stop":
    current_command = int(command)
    if min_number > current_command:
        min_number = current_command
    command = input()

print(min_number)
