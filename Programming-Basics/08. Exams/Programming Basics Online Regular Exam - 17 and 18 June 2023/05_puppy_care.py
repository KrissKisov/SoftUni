food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
command = input()
while command != "Adopted":
    current_food = int(command)
    food_in_grams -= current_food

    command = input()

if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {food_in_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(food_in_grams)} grams more.")
