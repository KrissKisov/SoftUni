given_numbers = tuple(float(x) for x in input().split())

numbers_dict = {k: 1 for k in given_numbers}
for number in numbers_dict.keys():
    print(f"{number} - {given_numbers.count(number)} times")
