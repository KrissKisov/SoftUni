some_string = input()
output_string = ""

current_string = ""
current_number = ""

for index, character in enumerate(some_string):
    if character.isnumeric():
        current_number += character
        if index == len(some_string) - 1:
            output_string += current_string.upper() * int(current_number)
    else:
        if len(current_number) > 0:
            output_string += current_string.upper() * int(current_number)
            current_number = ""
            current_string = character
        else:
            current_string += character

print(f"Unique symbols used: {len(set(output_string))}")
print(output_string)
