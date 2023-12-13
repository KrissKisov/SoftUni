number = int(input())
number_as_str = str(number)

for first_digit in range(1, int(number_as_str[2]) + 1):
    for second_digit in range(1, int(number_as_str[1]) + 1):
        for third_digit in range(1, int(number_as_str[0]) + 1):
            first_multiplier = first_digit
            second_multiplier = second_digit
            third_multiplier = third_digit
            result = first_multiplier * second_multiplier * third_multiplier
            print(f"{first_multiplier} * {second_multiplier} * {third_multiplier} = {result};")
