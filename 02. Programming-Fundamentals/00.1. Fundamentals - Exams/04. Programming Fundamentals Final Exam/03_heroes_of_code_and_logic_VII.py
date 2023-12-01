heroes = {}
max_hp = 100
max_mp = 200
number_of_heroes = int(input())
for _ in range(number_of_heroes):
    hero, hit_points, mana_points = input().split()
    heroes[hero] = []
    heroes[hero].append(int(hit_points))
    heroes[hero].append(int(mana_points))

command = input().split(" - ")
while command[0] != "End":
    hero_name = command[1]
    if command[0] == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3]
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        if heroes[hero_name][0] > damage:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        amount_mp = int(command[2])
        maximum_to_recharge = max_mp - heroes[hero_name][1]
        if maximum_to_recharge >= amount_mp:
            heroes[hero_name][1] += amount_mp
        else:
            heroes[hero_name][1] = max_mp
        print(f"{hero_name} recharged for {min(amount_mp, maximum_to_recharge)} MP!")

    elif command[0] == "Heal":
        amount_hp = int(command[2])
        maximum_to_heal = max_hp - heroes[hero_name][0]
        if maximum_to_heal >= amount_hp:
            heroes[hero_name][0] += amount_hp
        else:
            heroes[hero_name][0] = max_hp
        print(f"{hero_name} healed for {min(amount_hp, maximum_to_heal)} HP!")

    command = input().split(" - ")

for hero, hero_hp_mp in heroes.items():
    print(f"{hero}\n"
          f"  HP: {hero_hp_mp[0]}\n"
          f"  MP: {hero_hp_mp[1]}")
