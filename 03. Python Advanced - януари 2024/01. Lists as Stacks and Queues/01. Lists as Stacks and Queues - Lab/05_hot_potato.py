from collections import deque

kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    kids.rotate(-(toss - 1))
    # kid_to_remove = kids.popleft()
    # print(f"Removed {kid_to_remove}")
    print(f"Removed {kids.popleft()}")

print(f"Last is {''.join(kids)}")
# print(f"Last is {kids.pop()}")
