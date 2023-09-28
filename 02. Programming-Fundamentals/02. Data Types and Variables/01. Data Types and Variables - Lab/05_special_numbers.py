number = int(input())

for num in range(1, number + 1):
    num_as_str = str(num)
    sum_of_digit = 0
    for digit in num_as_str:
        sum_of_digit += int(digit)

    if sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
