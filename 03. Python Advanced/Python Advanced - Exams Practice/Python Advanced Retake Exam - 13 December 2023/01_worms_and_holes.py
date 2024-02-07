# # with comprehensions
# from collections import deque
#
#
# worms = [int(x) for x in input().split()]
# holes = deque(int(x) for x in input().split())
#
# matches = 0
# worms_to_fit = len(worms)
#
# while worms and holes:
#     worm = worms.pop()
#     hole = holes.popleft()
#
#     if worm == hole:
#         matches += 1
#         worms_to_fit -= 1
#         continue
#
#     worm -= 3
#
#     if worm <= 0:
#         continue
#
#     worms.append(worm)
#
# if matches != 0:
#     print(f"Matches: {matches}")
# else:
#     print("There are no matches.")
#
# if worms_to_fit == 0:
#     print("Every worm found a suitable hole!")
# elif not worms and worms_to_fit != 0:
#     print("Worms left: none")
# elif worms:
#     print(f"Worms left: {', '.join([str(x) for x in worms])}")
#
# if holes:
#     print(f"Holes left: {', '.join(str(x) for x in holes)}")
# else:
#     print("Holes left: none")


# without comprehensions
from collections import deque


worms = input().split()
holes = deque(input().split())

matches = 0
worms_to_fit = len(worms)

while worms and holes:
    worm = int(worms.pop())
    hole = int(holes.popleft())

    if worm == hole:
        matches += 1
        worms_to_fit -= 1
        continue

    worm -= 3

    if worm <= 0:
        continue

    worms.append(str(worm))

if matches != 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if worms_to_fit == 0:
    print("Every worm found a suitable hole!")
elif not worms and worms_to_fit != 0:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(worms)}")

if holes:
    print(f"Holes left: {', '.join(holes)}")
else:
    print("Holes left: none")
