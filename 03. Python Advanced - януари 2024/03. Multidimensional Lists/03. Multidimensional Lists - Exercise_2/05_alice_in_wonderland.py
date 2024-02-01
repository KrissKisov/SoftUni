number = int(input())

territory = []
alice = []
total_tes_bags = 0
movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(number):
    line = input().split()
    territory.append(line)

    if "A" in line:
        alice.extend([row, line.index("A")])

    if "R" in line:
        rabbit_hole = [row, line.index("R")]

territory[alice[0]][alice[1]] = "*"

while total_tes_bags < 10:
    direction = input()

    r, c = alice[0] + movements[direction][0], alice[1] + movements[direction][1]

    if r not in range(number) or c not in range(number):
        break

    alice = [r, c]

    if territory[r][c] == "R":
        territory[r][c] = "*"
        break

    elif territory[r][c].isdigit():
        total_tes_bags += int(territory[r][c])

    territory[r][c] = "*"

if total_tes_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for line in territory:
    print(*line)
