gifts = input().split()
command = input()

while command != "No Money":
    current_command = command.split()
    gift = current_command[1]

    if current_command[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == gift:
                gifts[index] = "None"

    elif current_command[0] == "Required":
        index = int(current_command[2])
        if index in range(len(gifts)):
            gifts[index] = gift

    elif current_command[0] == "JustInCase":
        gifts[-1] = gift

    command = input()

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))
