# number = input()
# number_as_list = []
#
# for num in number:
#     number_as_list.append(num)
#
# largets_number = "".join(sorted(number_as_list, reverse=True))
# print(largets_number)

number = list(input())
sorted_number = sorted(number, reverse=True)
largest_number = int("".join(sorted_number))
print(largest_number)
