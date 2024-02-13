from collections import deque


eggs_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = [int(x) for x in input().split(", ")]

boxes = 0

while eggs_sizes and paper_sizes:

    egg = eggs_sizes.popleft()

    if egg <= 0:
        continue

    elif egg == 13:
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue

    paper = paper_sizes.pop()

    if egg + paper <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sizes)}")

if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")
