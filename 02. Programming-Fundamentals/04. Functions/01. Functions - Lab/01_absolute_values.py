def absolut_value(numbers_list: list) -> list:
    absolut_value_list = []
    for number in numbers_list:
        absolut_value_list.append(abs(number))

    return absolut_value_list


list_of_numbers = list(map(float, (input().split())))
print(absolut_value(list_of_numbers))
