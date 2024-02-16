directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rows, columns = [int(x) for x in input().split(", ")]

matrix = []
position = []
num_of_all_items = 0
num_of_collected_items = 0
collected_items_dict = {
    "D": 0,
    "G": 0,
    "C": 0,
}

for row in range(rows):

    data = input().split()
    matrix.append(data)

    for symbol in data:

        if symbol == "Y":
            position = [row, data.index("Y")]

        elif symbol.isalpha():
            num_of_all_items += 1

command = input().split("-")

while "End" not in command:

    everything_is_collected = False
    direction, steps = command[0], int(command[1])

    for _ in range(steps):

        r = (position[0] + directions[direction][0] + rows) % rows
        c = (position[1] + directions[direction][1] + columns) % columns

        if matrix[r][c] in collected_items_dict:
            item = matrix[r][c]
            num_of_collected_items += 1
            collected_items_dict[item] += 1

        matrix[position[0]][position[1]] = "x"
        matrix[r][c] = "Y"
        position = [r, c]

        if num_of_collected_items == num_of_all_items:
            print("Merry Christmas!")
            everything_is_collected = True
            break

    if everything_is_collected:
        break

    command = input().split("-")

output_dict = {
    "D": f"- {collected_items_dict['D']} Christmas decorations",
    "G": f"- {collected_items_dict['G']} Gifts",
    "C": f"- {collected_items_dict['C']} Cookies",
}

print("You've collected:")
[print(output_dict[key]) for key in output_dict]
[print(*row) for row in matrix]
