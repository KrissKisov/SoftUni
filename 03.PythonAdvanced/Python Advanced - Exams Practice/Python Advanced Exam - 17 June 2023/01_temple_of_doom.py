from collections import deque


tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = deque([int(x) for x in input().split()])

while tools and substances:

    if not challenges:
        break

    result = tools[0] * substances[-1]

    for _ in range(len(challenges)):

        if result == challenges[0]:
            tools.popleft()
            substances.pop()
            challenges.popleft()
            break

        challenges.rotate(-1)

    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1

        if substances[-1] <= 0:
            substances.pop()

if (not tools or not substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

elif not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
