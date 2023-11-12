given_string = input()
output_string = given_string[0]
for index in range(1, len(given_string)):
    if given_string[index] != given_string[index - 1]:
        output_string += given_string[index]
print(output_string)
