number_of_visitors = int(input())

people_trained_back = 0
people_trained_chest = 0
people_trained_legs = 0
people_trained_abs = 0
people_bought_shake = 0
people_bought_bar = 0
total_training = 0
total_buying = 0

for visitor in range(number_of_visitors):
    action = input()  # "Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar"

    if action == "Back":
        people_trained_back += 1
        total_training += 1
    elif action == "Chest":
        people_trained_chest += 1
        total_training += 1
    elif action == "Legs":
        people_trained_legs += 1
        total_training += 1
    elif action == "Abs":
        people_trained_abs += 1
        total_training += 1
    elif action == "Protein shake":
        people_bought_shake += 1
        total_buying += 1
    else:  # action == "Protein bar"
        people_bought_bar += 1
        total_buying += 1

percent_training = total_training / number_of_visitors * 100
percent_buying = total_buying / number_of_visitors * 100

print(f"{people_trained_back} - back")
print(f"{people_trained_chest} - chest")
print(f"{people_trained_legs} - legs")
print(f"{people_trained_abs} - abs")
print(f"{people_bought_shake} - protein shake")
print(f"{people_bought_bar} - protein bar")
print(f"{percent_training :.2f}% - work out")
print(f"{percent_buying :.2f}% - protein")
