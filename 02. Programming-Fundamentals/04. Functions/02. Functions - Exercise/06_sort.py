# numbers_as_string = input().split()
# numbers_as_digit = sorted(map(int, numbers_as_string))
# print(numbers_as_digit)

numbers_as_string = input().split()
numbers_as_digit = []
for symbol in numbers_as_string:
    number = int(symbol)
    numbers_as_digit.append(number)

sorted_list = sorted(numbers_as_digit)
print(sorted_list)
