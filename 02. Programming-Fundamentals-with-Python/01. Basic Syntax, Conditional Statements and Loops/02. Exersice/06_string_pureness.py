number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()
    if ("," in current_string
            or "." in current_string
            or "_" in current_string):
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

# number_of_strings = int(input())
# not_pure_list = [",", ".", "_"]
#
# for string in range(number_of_strings):
#     current_string = input()
#     if any(symbol in current_string for symbol in not_pure_list):
#         print(f"{current_string} is not pure!")
#     else:
#         print(f"{current_string} is pure.")

# number_of_strings = int(input())
# not_pure_list = [",", ".", "_"]
#
# for string in range(number_of_strings):
#     current_string = input()
#     if any(symbol in not_pure_list for symbol in current_string):
#         print(f"{current_string} is not pure!")
#     else:
#         print(f"{current_string} is pure.")
