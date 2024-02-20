number_of_plants = int(input())
plants_dictionary = {}
for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    plants_dictionary[plant] = {"rarity": int(rarity)}

command = input().split(" ")
while "Exhibition" not in command[0]:
    if command[0] == "Rate:":
        current_plant = command[1]
        rating = int(command[3])

        if current_plant not in plants_dictionary.keys():
            print("error")
        else:
            if "rating" not in plants_dictionary[current_plant].keys():
                plants_dictionary[current_plant]["rating"] = []
            plants_dictionary[current_plant]["rating"].append(rating)

    elif command[0] == "Update:":
        plant_to_update = command[1]
        new_rarity = int(command[3])

        if plant_to_update not in plants_dictionary.keys():
            print("error")
        else:
            plants_dictionary[plant_to_update]["rarity"] = new_rarity

    elif command[0] == "Reset:":
        plant_to_reset = command[1]

        if plant_to_reset not in plants_dictionary.keys():
            print("error")
        else:
            plants_dictionary[plant_to_reset].pop("rating")

    command = input().split(" ")

print("Plants for the exhibition:")
for each_plant, plant_info in plants_dictionary.items():
    if "rating" not in plant_info.keys():
        average_rating = 0
        print(f"- {each_plant}; Rarity: {plant_info['rarity']}; Rating: {average_rating :.2f}")
    else:
        average_rating = sum(plant_info["rating"]) / len(plant_info["rating"])
        print(f"- {each_plant}; Rarity: {plant_info['rarity']}; Rating: {average_rating :.2f}")
