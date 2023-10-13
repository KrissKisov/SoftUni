# def tribonacci(some_number):
#     tribonacci_list = []
#     for num in range(1, some_number + 1):
#         if num < 2:
#             tribonacci_list.append(num)
#         elif num < 3:
#             tribonacci_list.append(num - 1)
#         elif num < 4:
#             tribonacci_list.append(tribonacci_list[-1] + tribonacci_list[-2])
#         else:
#             tribonacci_list.append(tribonacci_list[-1] + tribonacci_list[-2] + tribonacci_list[-3])
#     print(*tribonacci_list)
#
#
# number = int(input())
# tribonacci(number)


def tribonacci(some_number):
    tribonacci_list = []
    for num in range(1, some_number + 1):
        if num < 2:
            tribonacci_list.append(num)
        elif num < 3:
            tribonacci_list.append(num - 1)
        elif num < 4:
            tribonacci_list.append(tribonacci_list[-1] + tribonacci_list[-2])
        else:
            tribonacci_list.append(tribonacci_list[-1] + tribonacci_list[-2] + tribonacci_list[-3])
    result = " ".join(str(x) for x in tribonacci_list)
    return result


number = int(input())
print(tribonacci(number))
