dragons = {}
number_of_dragons = int(input())
for _ in range(number_of_dragons):
    dragon_type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)

    if health == "null":
        health = 250
    else:
        health = int(health)

    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    if dragon_type not in dragons.keys():
        dragons[dragon_type] = {}
    dragons[dragon_type][name] = [damage, health, armor]

for type_of_dragon, dragon_info in dragons.items():
    dragons[type_of_dragon] = dict(sorted(dragon_info.items(), key=lambda x: x[0]))

for type_of_dragon, dragon_info in dragons.items():
    dragons_count = len(dragon_info.keys())
    total_type_damage = 0
    total_type_health = 0
    total_type_armor = 0
    for current_dragon, stats in dragon_info.items():
        total_type_damage += stats[0]
        total_type_health += stats[1]
        total_type_armor += stats[2]

    average_damage = total_type_damage / dragons_count
    average_health = total_type_health / dragons_count
    average_armor = total_type_armor / dragons_count

    print(f"{type_of_dragon}::({average_damage :.2f}/{average_health :.2f}/{average_armor :.2f})")
    for current_dragon, stats in dragon_info.items():
        print(f"-{current_dragon} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
