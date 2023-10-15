def check_chairs(number_of_rooms: int):
    free_chairs_count = 0
    for room in range(1, number_of_rooms + 1):
        chairs_and_people = input().split(" ")
        chairs = len(chairs_and_people[0])
        people = int(chairs_and_people[1])
        if chairs < people:
            print(f"{people - chairs} more chairs needed in room {room}")
        free_chairs_count += chairs - people

    if free_chairs_count >= 0:
        return f"Game On, {free_chairs_count} free chairs left"
    else:
        exit()


rooms = int(input())
print(check_chairs(rooms))
