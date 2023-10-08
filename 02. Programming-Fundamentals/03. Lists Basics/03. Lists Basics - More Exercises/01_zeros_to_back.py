# numbers_as_string = input().split(", ")
# numbers_as_integers = list(map(int, numbers_as_string))
# for element in numbers_as_integers:
#     if element == 0:
#         numbers_as_integers.remove(element)
#         numbers_as_integers.append(element)
#
# print(numbers_as_integers)

input_number = list(map(int, input().split(", ")))

for _ in input_number:
    input_number.append(input_number.pop(input_number.index(0)))

print(input_number)
