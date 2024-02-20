# initial_list = input().split()
# initial_list_as_integers = list(map(int, initial_list))
# command = input()
#
# while command != "end":
#     current_command = command.split()
#     if current_command[0] == "exchange":
#         index = int(current_command[1])
#         if not 0 <= index <= len(initial_list_as_integers):
#             print("Invalid index")
#         else:
#             initial_list_as_integers = initial_list_as_integers[index + 1:] + initial_list_as_integers[:index + 1]
#
#     elif current_command[0] == "max":
#         if current_command[1] == "even":
#             count_even = [x for x in initial_list_as_integers if x % 2 == 0]
#             # count_even = list(x for x in initial_list_as_integers if x % 2 == 0)
#             if len(count_even) > 0:
#                 max_even = max(x for x in initial_list_as_integers if x % 2 == 0)
#                 print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(max_even) - 1)
#             else:
#                 print("No matches")
#         elif current_command[1] == "odd":
#             count_odd = [x for x in initial_list_as_integers if x % 2 != 0]
#             if len(count_odd) > 0:
#                 max_odd = max(x for x in initial_list_as_integers if x % 2 != 0)
#                 print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(max_odd) - 1)
#             else:
#                 print("No matches")
#
#     elif current_command[0] == "min":
#         if current_command[1] == "even":
#             count_even = [x for x in initial_list_as_integers if x % 2 == 0]
#             if len(count_even) > 0:
#                 min_even = min(x for x in initial_list_as_integers if x % 2 == 0)
#                 print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(min_even) - 1)
#             else:
#                 print("No matches")
#         elif current_command[1] == "odd":
#             count_odd = [x for x in initial_list_as_integers if x % 2 != 0]
#             if len(count_odd) > 0:
#                 min_odd = min(x for x in initial_list_as_integers if x % 2 != 0)
#                 print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(min_odd) - 1)
#             else:
#                 print("No matches")
#
#     elif current_command[0] == "first":
#         counter = int(current_command[1])
#         if counter <= len(initial_list_as_integers):
#             if current_command[2] == "even":
#                 even_numbers_count = [x for x in initial_list_as_integers if x % 2 == 0]
#                 print(even_numbers_count[:counter])
#             elif current_command[2] == "odd":
#                 odd_numbers_count = [x for x in initial_list_as_integers if x % 2 != 0]
#                 print(odd_numbers_count[:counter])
#         else:  # counter > len(initial_list_as_integers):
#             print("Invalid count")
#
#     elif current_command[0] == "last":
#         counter = int(current_command[1])
#         if counter <= len(initial_list_as_integers):
#             if current_command[2] == "even":
#                 even_numbers_count = [x for x in initial_list_as_integers if x % 2 == 0]
#                 print(even_numbers_count[-counter:])
#             elif current_command[2] == "odd":
#                 odd_numbers_count = [x for x in initial_list_as_integers if x % 2 != 0]
#                 print(odd_numbers_count[-counter:])
#         else:  # counter > len(initial_list_as_integers):
#             print("Invalid count")
#
#     command = input()
#
# print(initial_list_as_integers)

####################

initial_list = input().split()
initial_list_as_integers = list(map(int, initial_list))
command = input()

while command != "end":
    current_command = command.split()
    if current_command[0] == "exchange":
        index = int(current_command[1])
        if 0 < index <= len(initial_list_as_integers):
            initial_list_as_integers = initial_list_as_integers[index + 1:] + initial_list_as_integers[:index + 1]
        else:
            print("Invalid index")

    elif current_command[0] == "max":
        if current_command[1] == "even":
            count_even = [x for x in initial_list_as_integers if x % 2 == 0]
            # count_even = list(x for x in initial_list_as_integers if x % 2 == 0)
            if len(count_even) > 0:
                max_even = max(x for x in initial_list_as_integers if x % 2 == 0)
                print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(max_even) - 1)
            else:
                print("No matches")
        elif current_command[1] == "odd":
            count_odd = [x for x in initial_list_as_integers if x % 2 != 0]
            if len(count_odd) > 0:
                max_odd = max(x for x in initial_list_as_integers if x % 2 != 0)
                print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(max_odd) - 1)
            else:
                print("No matches")

    elif current_command[0] == "min":
        if current_command[1] == "even":
            count_even = [x for x in initial_list_as_integers if x % 2 == 0]
            if len(count_even) > 0:
                min_even = min(x for x in initial_list_as_integers if x % 2 == 0)
                print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(min_even) - 1)
            else:
                print("No matches")
        elif current_command[1] == "odd":
            count_odd = [x for x in initial_list_as_integers if x % 2 != 0]
            if len(count_odd) > 0:
                min_odd = min(x for x in initial_list_as_integers if x % 2 != 0)
                print(len(initial_list_as_integers) - initial_list_as_integers[::-1].index(min_odd) - 1)
            else:
                print("No matches")

    elif current_command[0] == "first":
        counter = int(current_command[1])
        if 0 <= counter <= len(initial_list_as_integers):
            if current_command[2] == "even":
                even_numbers_count = [x for x in initial_list_as_integers if x % 2 == 0]
                print(even_numbers_count[:counter])
            elif current_command[2] == "odd":
                odd_numbers_count = [x for x in initial_list_as_integers if x % 2 != 0]
                print(odd_numbers_count[:counter])
        else:  # counter > len(initial_list_as_integers):
            print("Invalid count")

    elif current_command[0] == "last":
        counter = int(current_command[1])
        if 0 <= counter <= len(initial_list_as_integers):
            if current_command[2] == "even":
                even_numbers_count = [x for x in initial_list_as_integers if x % 2 == 0]
                print(even_numbers_count[-counter:])
            elif current_command[2] == "odd":
                odd_numbers_count = [x for x in initial_list_as_integers if x % 2 != 0]
                print(odd_numbers_count[-counter:])
        else:  # counter > len(initial_list_as_integers):
            print("Invalid count")

    command = input()

print(initial_list_as_integers)
