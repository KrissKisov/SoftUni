# solution 1
string_of_numbers = input().split("|")

flatten_list = [int(x) for sub_list in reversed(string_of_numbers) for x in sub_list.split()]
print(*flatten_list)

## solution 2
# print(*[int(x) for sub_list in reversed(input().split("|")) for x in sub_list.split()])

## solution 3
# string_of_numbers = input().split("|")
#
# flatten_list = []
#
# for sub_list in reversed(string_of_numbers):
#     flatten_list.extend(int(x) for x in sub_list.split())
#
# print(*flatten_list)
