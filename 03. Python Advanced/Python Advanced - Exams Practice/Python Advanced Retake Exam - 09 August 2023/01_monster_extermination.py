from collections import deque


monster_armors = deque(int(x) for x in input().split(","))
striking_impacts = [int(x) for x in input().split(",")]

killed_monsters = 0

while monster_armors and striking_impacts:
    strike = striking_impacts.pop()
    armor = monster_armors.popleft()
    if strike >= armor:
        killed_monsters += 1
        strike -= armor
        if striking_impacts:
            strike += striking_impacts.pop()
            striking_impacts.append(strike)
        else:
            if strike != 0:
                striking_impacts.append(strike)
    elif strike < armor:
        armor -= strike
        monster_armors.append(armor)

if not monster_armors:
    print("All monsters have been killed!")

if not striking_impacts:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
