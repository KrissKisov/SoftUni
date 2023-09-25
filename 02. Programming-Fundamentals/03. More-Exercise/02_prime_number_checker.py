# number = int(input())
# is_prime = True
#
# for digit in range(1, number + 1):
#
#     if digit > 1:
#
#         for num in range(2, digit):
#
#             if digit % num == 0:
#                 is_prime = False
#                 break
#         else:
#             is_prime = True
#
#     else:
#         continue
# print(is_prime)

number = int(input())
is_prime = True
if number > 1:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
    else:
        is_prime = True
print(is_prime)
