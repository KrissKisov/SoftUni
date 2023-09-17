beginning = input()# int(input())
ending = input()#int(input())

# for barcode in range(beginning, ending + 1):
#     for digit_1 in range(barcode // 1000, barcode // 1000 + 1):
#         for digit_2 in range(barcode // 100 % 10, barcode // 100 % 10 + 1):
#             for digit_3 in range(barcode % 100 // 10, barcode % 100 // 10 + 1):
#                 for digit_4 in range(barcode % 10, barcode % 10 + 1):
#                     if digit_1 % 2 != 0 and digit_2 % 2 != 0 and digit_3 % 2 != 0 and digit_4 % 2 != 0:
#                         print(barcode, end=" ")

for digit_one in range(int(beginning[0]), int(ending[0]) + 1):
    for digit_two in range(int(beginning[1]), int(ending[1]) + 1):
        for digit_three in range(int(beginning[2]), int(ending[2]) + 1):
            for digit_four in range(int(beginning[3]), int(ending[3]) + 1):
                if digit_one % 2 != 0 and digit_two % 2 != 0 and digit_three % 2 != 0 and digit_four % 2 != 0:
                    print(f"{digit_one}{digit_two}{digit_three}{digit_four}", end=" ")
