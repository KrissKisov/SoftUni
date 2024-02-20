from collections import deque


bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())

num_of_tries = 0

while bullets and locks:
    num_of_tries += 1

    current_lock = locks.popleft()
    current_bullet = bullets.pop()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    intelligence_value -= bullet_price

    if bullets:
        if num_of_tries % barrel_size == 0:
            print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
