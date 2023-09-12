bought_food_kg = int(input())
food_in_grams = bought_food_kg * 1000
command = input()

while command != "Adopted":
    eaten_food_daily = int(command)
    food_in_grams -= eaten_food_daily

    command = input()

leftover_food = food_in_grams
if leftover_food >= 0:
    print(f"Food is enough! Leftovers: {leftover_food} grams.")
else:
    print(f"Food is not enough. You need {abs(leftover_food)} grams more.")
