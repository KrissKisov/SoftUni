first_number = int(input())
second_number = int(input())
third_number = int(input())
is_even = True
is_prime = True
for digit_1 in range(1, first_number + 1):

    if digit_1 % 2 != 0:
        is_even = False
        continue

    for digit_2 in range(1, second_number + 1):

        if digit_2 > 1:

            for num in range(2, digit_2):

                if digit_2 % num == 0:
                    is_prime = False
                    break
            else:
                is_prime = True

        else:
            continue

        for digit_3 in range(1, third_number + 1):

            if digit_3 % 2 != 0:
                is_even = True
                continue
            if is_even and is_prime:
                print(f"{digit_1} {digit_2} {digit_3}")
