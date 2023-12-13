phonebook = {}

while True:
    input_line = input()
    if '-' not in input_line:
        break

    name, phone_number = input_line.split('-')
    phonebook.update({name: phone_number})
    # name, phone_number = input_line.split('-')
    # phonebook[name] = phone_number

number = int(input_line)
for i in range(number):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
