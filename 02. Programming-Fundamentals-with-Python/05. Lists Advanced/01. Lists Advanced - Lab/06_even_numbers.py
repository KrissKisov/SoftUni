# number_list = input().split(", ")
# even_num = []
# for number in range(len(number_list)):
#     current_num = int(number_list[number])
#     if current_num % 2 == 0:
#         even_num.append(number)
#
# print(even_num)

number_list = input().split(", ")
even_num = [number for number in range(len(number_list)) if int(number_list[number]) % 2 == 0]
print(even_num)
