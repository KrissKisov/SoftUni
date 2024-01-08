food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
weight_in_kg = float(input())
shopping_needed = False

for day in range(1, 31):
    food_in_kg -= 0.3

    if food_in_kg < 0.3:
        shopping_needed = True
        break

    if day % 2 == 0:
        if hay_in_kg - (food_in_kg * 0.05) > 0:
            hay_in_kg -= food_in_kg * 0.05
        else:
            shopping_needed = True
            break

    if day % 3 == 0:
        if cover_in_kg - (weight_in_kg / 3) > 0:
            cover_in_kg -= weight_in_kg / 3
        else:
            shopping_needed = True
            break

if shopping_needed:
    print("Merry must go to the pet store!")
else:
    print(
        f"Everything is fine! Puppy is happy! Food: {food_in_kg :.2f}, Hay: {hay_in_kg :.2f}, Cover: {cover_in_kg :.2f}.")
