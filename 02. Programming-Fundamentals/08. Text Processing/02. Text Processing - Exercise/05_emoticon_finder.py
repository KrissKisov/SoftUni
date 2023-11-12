input_line = input()
for index, char in enumerate(input_line):
    if char == ":":
        print(char + input_line[index + 1])
