directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
MAXIMUM_HITS = 3
CRUISERS = 3
hits = 0
sunk_cruisers = 0
submarine_pos = None

n = int(input())

battlefield = []

for i in range(n):
    field = list(input())
    battlefield.append(field)

    if "S" in field:
        submarine_pos = [i, field.index("S")]
        battlefield[submarine_pos[0]][submarine_pos[1]] = "-"

while True:

    direction = input()

    r, c = submarine_pos[0] + directions[direction][0], submarine_pos[1] + directions[direction][1]

    if battlefield[r][c] == "*":
        battlefield[r][c] = "-"
        submarine_pos = [r, c]
        hits += 1

        if hits == MAXIMUM_HITS:
            battlefield[r][c] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            break

    elif battlefield[r][c] == "C":
        battlefield[r][c] = "-"
        submarine_pos = [r, c]
        sunk_cruisers += 1

        if sunk_cruisers == CRUISERS:
            battlefield[r][c] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    elif battlefield[r][c] == "-":
        submarine_pos = [r, c]

for row in battlefield:
    print(''.join(row))
