# numbers_list = list(map(int, input().split()))
# print(f"The minimum number is {min(numbers_list)}")
# print(f"The maximum number is {max(numbers_list)}")
# print(f"The sum number is: {sum(numbers_list)}")
def min_number(numbers_list: list) -> int:
    numbers_as_digit = []
    for number in numbers_list:
        numbers_as_digit.append(int(number))

    return min(numbers_as_digit)


def max_number(numbers_list: list) -> int:
    numbers_as_digit = [int(num) for num in numbers_list]

    return max(numbers_as_digit)


def sum_number(numbers_list: list) -> int:
    numbers_as_digit = list(map(int, numbers_list))

    return sum(numbers_as_digit)


numbers_as_string = input().split()
smallest = min_number(numbers_as_string)
biggest = max_number(numbers_as_string)
sum_of_all = sum_number(numbers_as_string)

print(f"The minimum number is {smallest}")
print(f"The maximum number is {biggest}")
print(f"The sum number is: {sum_of_all}")
