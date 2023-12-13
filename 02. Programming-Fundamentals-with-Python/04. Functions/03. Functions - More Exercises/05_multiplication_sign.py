def multiplication_result(first: int, second: int, third: int) -> str:
    numbers_list = [first, second, third]
    negatives_count = 0
    have_zero = False
    for number in numbers_list:
        if number < 0:
            negatives_count += 1
        elif number == 0:
            have_zero = True

    if have_zero:
        result = "zero"
    elif negatives_count % 2 != 0:
        result = "negative"
    else:
        result = "positive"

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication_result(first_number, second_number, third_number))
