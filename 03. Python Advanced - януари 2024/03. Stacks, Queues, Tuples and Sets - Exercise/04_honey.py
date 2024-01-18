from collections import deque

bees_queue = deque(input().split())
nectar_queue = deque(input().split())
symbols_queue = deque(input().split())

total_honey = 0

while bees_queue and nectar_queue:
    bee = int(bees_queue.popleft())
    nectar = int(nectar_queue.pop())

    if nectar >= bee:
        symbol = symbols_queue.popleft()
        if symbol == "/" and nectar == 0:
            continue

        total_honey += abs(eval(f"{bee}{symbol}{nectar}"))

    else:
        bees_queue.appendleft(str(bee))

print(f"Total honey made: {total_honey}")
if bees_queue:
    print(f"Bees left: {', '.join(bees_queue)}")
if nectar_queue:
    print(f"Nectar left: {', '.join(nectar_queue)}")
