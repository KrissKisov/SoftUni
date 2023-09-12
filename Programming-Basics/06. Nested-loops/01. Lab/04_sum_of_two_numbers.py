start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_count = 0
first_number = 0
second_number = 0
is_magic_found = False
for num_1 in range(start_number, end_number + 1):
    first_number = num_1
    for num_2 in range(start_number, end_number + 1):
        second_number = num_2
        combination_count += 1
        if num_1 + num_2 == magic_number:
            is_magic_found = True
            # print(f"Combination N:{combination_count} ({num_1} + {num_2} = {magic_number})")
            break
    if is_magic_found:
        break
if is_magic_found:
    print(f"Combination N:{combination_count} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")
