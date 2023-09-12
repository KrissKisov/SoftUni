starting_number = int(input())
ending_number = int(input())
magic_number = int(input())
is_magic_found = False
combination = 0
first_number = 0
second_number = 0
for first_num in range(starting_number, ending_number + 1):
    first_number = first_num
    for second_num in range(starting_number, ending_number + 1):
        second_number = second_num
        combination += 1

        if first_num + second_num == magic_number:
            is_magic_found = True
            break

    if is_magic_found:
        break

if is_magic_found:
    print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
