from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")

robots_process_time = {}
robots_until_free = {}

for robot in robots:
    name, process_time = robot.split("-")
    robots_process_time[name] = int(process_time)
    robots_until_free[name] = 0

start_time = input()

start_time = datetime.strptime(start_time, "%H:%M:%S")

products = deque()

product = input()
while product != "End":
    products.append(product)

    product = input()

while products:
    current_product = products.popleft()
    start_time += timedelta(0, 1)

    available_robots = []
    for robot in robots_until_free:
        if robots_until_free[robot] == 0:
            available_robots.append((robot, robots_until_free[robot]))

        if robots_until_free[robot] != 0:
            robots_until_free[robot] -= 1

    if not available_robots:
        products.append(current_product)

    else:

        name = available_robots[0][0]
        print(f"{name} - {current_product} [{datetime.strftime(start_time, '%H:%M:%S')}]")
        robots_until_free[name] = robots_process_time[name] - 1
