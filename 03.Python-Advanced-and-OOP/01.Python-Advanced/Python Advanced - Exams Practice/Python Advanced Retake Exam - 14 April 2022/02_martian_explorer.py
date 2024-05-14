from collections import deque

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
size = 6
matrix = []
current_pos = []

for i in range(size):
    line = input().split()
    matrix.append(line)

    if "E" in line:
        current_pos = [i, line.index("E")]

deposits = {"W": 0, "M": 0, "C": 0}

commands = deque(input().split(", "))

while commands:
    command = commands.popleft()
    r = current_pos[0] + directions[command][0]
    c = current_pos[1] + directions[command][1]
    if r not in range(size):
        r = (r + size) % size
    elif c not in range(size):
        c = (c + size) % size

    if matrix[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

    elif matrix[r][c] == "W":
        deposits["W"] += 1
        print(f"Water deposit found at ({r}, {c})")

    elif matrix[r][c] == "M":
        deposits["M"] += 1
        print(f"Metal deposit found at ({r}, {c})")

    elif matrix[r][c] == "C":
        deposits["C"] += 1
        print(f"Concrete deposit found at ({r}, {c})")

    current_pos = [r, c]

is_suitable = True
for deposit, value in deposits.items():

    if deposits[deposit] == 0:
        is_suitable = False

if is_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
