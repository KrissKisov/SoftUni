field_size = 5
field = []
position = []
total_targets = 0
shoot_targets = []

for row in range(field_size):
    field.append(input().split())

    if "A" in field[row]:
        position = [row, field[row].index("A")]

    if "x" in field[row]:
        total_targets += field[row].count("x")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action, direction = command[0], command[1]

    if action == "move":
        steps = int(command[2])

        r, c = position[0] + directions[direction][0] * steps, position[1] + directions[direction][1] * steps

        if r not in range(field_size) or c not in range(field_size):
            r, c = position[0], position[1]

        elif field[r][c] == "x":
            r, c = position[0], position[1]

        else:
            position = [r, c]

    elif action == "shoot":
        r, c = position[0] + directions[direction][0], position[1] + directions[direction][1]

        while r in range(field_size) and c in range(field_size):

            if field[r][c] == "x":
                field[r][c] = "."
                shoot_targets.append([r, c])
                total_targets -= 1
                break

            r += directions[direction][0]
            c += directions[direction][1]

        if not total_targets:
            print(f"Training completed! All {len(shoot_targets)} targets hit.")
            break

if total_targets:
    print(f"Training not completed! {total_targets} targets left.")

print(*shoot_targets, sep="\n")
