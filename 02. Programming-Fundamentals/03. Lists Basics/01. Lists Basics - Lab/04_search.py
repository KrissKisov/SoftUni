number_of_strings = int(input())
special_word = input()
list_of_strings = []
special_list = []
for _ in range(number_of_strings):
    current_string = input()
    list_of_strings.append(current_string)

    if special_word in current_string:
        special_list.append(current_string)

print(list_of_strings)
print(special_list)
