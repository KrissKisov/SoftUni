first_string = input()
second_string = input()
unique_string = first_string

for index in range(len(first_string)):
    new_string = second_string[:index + 1] + first_string[index + 1:]

    if new_string != unique_string:
        unique_string = new_string
        print(unique_string)
