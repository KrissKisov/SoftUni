from math import inf

command = input()

max_number = float(-inf)
while command != "Stop":
    current_command = int(command)
    if max_number < current_command:
        max_number = current_command
    command = input()
print(max_number)
