from collections import deque

programmers_times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

ducky_types = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while programmers_times or tasks:
    current_time = programmers_times[0]
    current_task = tasks[-1]
    result = current_time * current_task

    if result > 240:
        tasks[-1] -= 2
        programmers_times.rotate(-1)
        continue

    if result <= 60:
        ducky_types["Darth Vader Ducky"] += 1

    elif result <= 120:
        ducky_types["Thor Ducky"] += 1

    elif result <= 180:
        ducky_types["Big Blue Rubber Ducky"] += 1

    elif result <= 240:
        ducky_types["Small Yellow Rubber Ducky"] += 1

    programmers_times.popleft()
    tasks.pop()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in ducky_types.items():
    print(f"{key}: {value}")
