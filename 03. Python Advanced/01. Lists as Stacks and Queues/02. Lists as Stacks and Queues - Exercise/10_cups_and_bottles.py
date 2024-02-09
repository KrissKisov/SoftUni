from collections import deque


cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:

    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup == current_bottle:
        continue

    elif current_cup > current_bottle:
        current_cup -= current_bottle
        cups.appendleft(current_cup)

    elif current_bottle > current_cup:
        wasted_water += current_bottle - current_cup

if not cups:
    print(f"Bottles:", *bottles[::-1])
    # print(f"Bottles: {' '.join([str(x) for x in bottles][::-1])}")

elif not bottles:
    print(f"Cups:", *cups)
    # print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")
