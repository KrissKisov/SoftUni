def shoot_target(given_index: int, given_power: int, targets: list) -> list:
    if given_index not in range(len(targets)):
        return targets
    targets[given_index] -= given_power
    if targets[given_index] <= 0:
        targets.pop(given_index)
    return targets


def add_targets(given_index: int, given_value: int, targets: list) -> list:
    if given_index not in range(len(targets)):
        print("Invalid placement!")
        return targets
    targets.insert(given_index, given_value)
    return targets


def strike_target(given_index: int, given_radius: int, targets: list) -> list:
    if (given_index not in range(len(targets))
            or given_index - given_radius not in range(len(targets))
            or given_index + given_radius not in range(len(targets))):
        print("Strike missed!")
        return targets
    return targets[:(given_index - given_radius)] + targets[(given_index + given_radius) + 1:]


targets_as_string = input().split()
targets_as_integers = list(map(int, targets_as_string))
command = input()

while command != "End":
    current_command = command.split()
    index = int(current_command[1])
    power = int(current_command[2])
    value = int(current_command[2])
    radius = int(current_command[2])

    if current_command[0] == "Shoot":
        targets_as_integers = shoot_target(index, power, targets_as_integers)

    elif current_command[0] == "Add":
        targets_as_integers = add_targets(index, value, targets_as_integers)

    elif current_command[0] == "Strike":
        targets_as_integers = strike_target(index, radius, targets_as_integers)

    command = input()

print(*targets_as_integers, sep="|")
