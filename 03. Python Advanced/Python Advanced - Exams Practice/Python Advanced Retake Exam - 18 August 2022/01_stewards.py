from collections import deque


seats = input().split(", ")
first_queue = deque([int(x) for x in input().split(", ")])
second_queue = deque([int(x) for x in input().split(", ")])

matched_seats_list = []
rotations = 0

while len(matched_seats_list) < 3 and rotations < 10:

    rotations += 1
    first_number = first_queue.popleft()
    second_number = second_queue.pop()
    letter = chr(first_number + second_number)

    if str(first_number) + letter in seats:

        if str(first_number) + letter not in matched_seats_list:
            matched_seats_list.append(str(first_number) + letter)
            continue

        else:
            continue

    elif str(second_number) + letter in seats:

        if str(second_number) + letter not in matched_seats_list:
            matched_seats_list.append(str(second_number) + letter)
            continue

        else:
            continue

    first_queue.append(first_number)
    second_queue.appendleft(second_number)

print(f"Seat matches: {', '.join(matched_seats_list)}")
print(f"Rotations count: {rotations}")
