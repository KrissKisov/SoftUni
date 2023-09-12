number = int(input())

for num in range(1_111, 10_000):
    current_number = str(num)

    is_special = True
    for index, char in enumerate(current_number):
        digit = int(char)

        if digit == 0:
            is_special = False
            break

        if number % digit != 0:
            is_special = False

    if is_special:
        print(int(current_number), end=" ")
