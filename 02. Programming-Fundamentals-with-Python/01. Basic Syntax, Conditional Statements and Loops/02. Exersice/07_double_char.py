while True:
    current_string = input()

    if current_string == "End":
        break

    if current_string == "SoftUni":
        continue

    for char in current_string:
        print(char * 2, end="")
    print()
