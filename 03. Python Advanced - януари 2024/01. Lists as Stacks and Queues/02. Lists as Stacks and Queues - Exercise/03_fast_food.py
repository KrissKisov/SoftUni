from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

for order in orders.copy():
    if food >= order:
        food -= order
        orders.popleft()
    else:
        print("Orders left:", *orders)
        break
else:
    print("Orders complete")
