cities = {}
info_cities = input()
while info_cities != "Sail":
    city, population, gold = info_cities.split("||")
    if city not in cities.keys():
        cities[city] = {"population": int(population), "gold": int(gold)}

    else:
        cities[city]["population"] += int(population)
        cities[city]["gold"] += int(gold)
    info_cities = input()

action_command = input().split("=>")
while action_command[0] != "End":
    action, town = action_command[0], action_command[1]
    if action == "Plunder":
        people, gold = int(action_command[2]), int(action_command[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        gold = int(action_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    action_command = input().split("=>")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, values in cities.items():
        print(f"{town} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
