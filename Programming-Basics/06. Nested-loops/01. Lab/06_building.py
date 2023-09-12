floors_count = int(input())
rooms_count = int(input())

for current_floor in range(floors_count, 0, -1):
    for current_room in range(rooms_count):

        if current_floor == floors_count:
            print(f"L{current_floor}{current_room}", end=" ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end=" ")
        else:
            print(f"A{current_floor}{current_room}", end=" ")
    print()
