NUMBER_OF_ENEMIES = 4

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())

airspace = []
position = []
armor = 300
shot_enemies = 0

for i in range(size):
    data = list(input())
    airspace.append(data)

    if "J" in data:
        position = [i, data.index("J")]
        airspace[i][data.index("J")] = "-"

while True:
    command = input()

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if airspace[r][c] == "R":
        armor = 300
        airspace[r][c] = "-"

    elif airspace[r][c] == "E":
        airspace[r][c] = "-"
        shot_enemies += 1

        if shot_enemies == NUMBER_OF_ENEMIES:
            print("Mission accomplished, you neutralized the aerial threat!")
            airspace[position[0]][position[1]] = "-"
            airspace[r][c] = "J"
            break

        armor -= 100
        if armor == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
            airspace[position[0]][position[1]] = "-"
            airspace[r][c] = "J"
            break

    position = [r, c]

[print(''.join(line)) for line in airspace]
