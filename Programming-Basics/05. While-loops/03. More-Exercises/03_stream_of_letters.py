command = input()

# "c", "o" и "n".
c_count = 0
o_count = 0
n_count = 0
word = ""
result = ""
while command != "End":
    if not command.isalpha():
        command = input()
        continue

    if command == "c":
        if c_count < 1:
            c_count += 1
            # command = input()
            # continue
        else:
            word += command

    elif command == "o":
        if o_count < 1:
            o_count += 1
            # command = input()
            # continue
        else:
            word += command

    elif command == "n":
        if n_count < 1:
            n_count += 1
            # command = input()
            # continue
        else:
            word += command

    else:
        word += command

    if c_count > 0 and o_count > 0 and n_count > 0:
        c_count = 0
        o_count = 0
        n_count = 0
        word += " "
        result = f"{word}"

    command = input()

print(result)
