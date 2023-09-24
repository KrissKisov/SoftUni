lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shields = 0
broken_armors = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
        if fight % 2 == 0:
            broken_shields += 1
            expenses += shield_price
            if broken_shields >= 2 and broken_shields % 2 == 0:
                broken_armors += 1
                expenses += armor_price

print(f"Gladiator expenses: {expenses :.2f} aureus")
