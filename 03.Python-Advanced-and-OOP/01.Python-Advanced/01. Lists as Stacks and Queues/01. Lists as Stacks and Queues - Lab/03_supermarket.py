from collections import deque

name = input()
queue = deque()

while name != "End":
    if name != "Paid":
        queue.append(name)
    else:
        while queue:
            print(queue.popleft())

    name = input()
print(f"{len(queue)} people remaining.")
