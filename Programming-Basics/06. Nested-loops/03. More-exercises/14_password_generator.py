# number_n = int(input())
# number_l = int(input())
#
# for first_symbol in range(1, number_n + 1):
#     for second_symbol in range(1, number_n + 1):
#         for third_symbol in range(97, 97 + number_l):
#             for fourth_symbol in range(97, 97 + number_l):
#                 for fifth_symbol in range(1, number_n + 1):
#                     if fifth_symbol > first_symbol and fifth_symbol > second_symbol:
#                         print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(fourth_symbol)}{fifth_symbol}", end=" ")

number_n = int(input())
number_l = int(input())

for first_symbol in range(1, number_n + 1):
    for second_symbol in range(1, number_n + 1):
        for third_symbol in range(ord("a"), ord("a") + number_l):
            for fourth_symbol in range(ord("a"), ord("a") + number_l):
                for fifth_symbol in range(1, number_n + 1):
                    if fifth_symbol > first_symbol and fifth_symbol > second_symbol:
                        print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(fourth_symbol)}{fifth_symbol}",
                              end=" ")
