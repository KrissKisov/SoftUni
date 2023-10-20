elements = input().split()
moves = 0
command = input()
while command != "end":
    moves += 1
    string = command.split()
    first_index = int(string[0])
    second_index = int(string[1])
    middle = len(elements) // 2
    to_add = f"-{moves}a"
    to_remove = max(first_index, second_index)
    to_pop = min(first_index, second_index)
    if first_index not in range(len(elements)):
        elements.insert(middle, to_add)
        elements.insert(middle, to_add)
        print("Invalid input! Adding additional elements to the board")
    elif second_index not in range(len(elements)):
        elements.insert(middle, to_add)
        elements.insert(middle, to_add)
        print("Invalid input! Adding additional elements to the board")
    elif first_index == second_index:
        elements.insert(middle, to_add)
        elements.insert(middle, to_add)
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements.pop(to_remove)
        elements.pop(to_pop)
    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    if len(elements) <= 0:
        break

    command = input()

if command == "end":
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")
else:
    print(f"You have won in {moves} turns!")
