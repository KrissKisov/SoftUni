numbers_list = [int(x) for x in input().split()]
command = input()
while command != "end":
    current_command = command.split()
    task = current_command[0]
    if task == "swap":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        numbers_list[first_index], numbers_list[second_index] = numbers_list[second_index], numbers_list[first_index]
    elif task == "multiply":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        numbers_list[first_index] = numbers_list[first_index] * numbers_list[second_index]
    elif task == "decrease":
        for element in range(len(numbers_list)):
            numbers_list[element] -= 1

    command = input()

print(", ".join(map(str, numbers_list)))
