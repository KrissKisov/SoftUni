size = int(input())
tracked_car = input()

race_route_matrix = []
current_pos = [0, 0]
tunnel_positions = []
passed_km = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(size):
    data = input().split()
    race_route_matrix.append(data)

    if data.count("T") == 1:
        tunnel_positions.append((i, data.index("T")))

    elif data.count("T") > 1:

        for index, symbol in enumerate(data):

            if symbol == "T":
                tunnel_positions.append((i, index))

command = input()

while True:

    if command == "End":
        print(f"Racing car {tracked_car} DNF.")
        race_route_matrix[current_pos[0]][current_pos[1]] = "C"
        break

    row, col = current_pos[0] + directions[command][0], current_pos[1] + directions[command][1]

    if race_route_matrix[row][col] == ".":
        passed_km += 10
        current_pos = [row, col]

    elif race_route_matrix[row][col] == "T":
        passed_km += 30
        current_pos = [tunnel_positions[1][0], tunnel_positions[1][1]]
        race_route_matrix[tunnel_positions[0][0]][tunnel_positions[0][1]] = "."
        race_route_matrix[tunnel_positions[1][0]][tunnel_positions[1][1]] = "."

    elif race_route_matrix[row][col] == "F":
        passed_km += 10
        race_route_matrix[row][col] = "C"
        print(f"Racing car {tracked_car} finished the stage!")
        break

    command = input()

print(f"Distance covered {passed_km} km.")

for line in race_route_matrix:
    print(*line, sep="")
