some_string = input()
command = input().split(" ")
while command[0] != "Done":
    action = command[0]
    if action == "TakeOdd":
        new_string = ""
        for index, char in enumerate(some_string):
            if index % 2 != 0:
                new_string += char
        some_string = new_string
        print(some_string)

    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        some_string = some_string[:index] + some_string[index + length:]
        print(some_string)

    elif action == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in some_string:
            some_string = some_string.replace(substring, substitute)
            print(some_string)
        else:
            print("Nothing to replace!")

    command = input().split(" ")
print(f"Your password is: {some_string}")
