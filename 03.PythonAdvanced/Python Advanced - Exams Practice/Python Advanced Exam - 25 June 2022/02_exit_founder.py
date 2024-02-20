from collections import deque


players = input().split(", ")

maze = []

for _ in range(6):
    maze.append(input().split())

player_needs_rest = deque()
turns = 0

while True:

    turns += 1
    coordinates = input()[1:-1].split(", ")
    r, c = int(coordinates[0]), int(coordinates[1])

    if turns % 2 != 0:
        current_player = players[0]
        next_player = players[1]

    else:
        current_player = players[1]
        next_player = players[0]

    if player_needs_rest:
        if current_player == player_needs_rest[0]:
            player_needs_rest.popleft()
            continue

    if maze[r][c] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        exit()

    elif maze[r][c] == "T":
        print(f"{current_player} is out of the game! The winner is {next_player}.")
        exit()

    elif maze[r][c] == "W":
        player_needs_rest.append(current_player)
        print(f"{current_player} hits a wall and needs to rest.")
