input_string = input()
string_as_list = list(input_string.split(" "))
opposite_numbers_list = []
for number in range(len(string_as_list)):
    opposite_number = int(string_as_list[number]) * -1
    opposite_numbers_list.append(opposite_number)

print(opposite_numbers_list)
