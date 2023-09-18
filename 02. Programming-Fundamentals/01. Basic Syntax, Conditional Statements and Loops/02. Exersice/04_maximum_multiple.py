divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        print(number)
        break

# divisor = int(input())
# boundary = int(input())
# needed_number = []
#
# for num in range(divisor, boundary + 1):
#     if num % divisor == 0:
#         needed_number.append(num)
#
# print(max(needed_number))
