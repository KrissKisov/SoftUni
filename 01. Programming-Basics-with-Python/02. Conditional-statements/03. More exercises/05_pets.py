from math import ceil, floor

count_days = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())
turtle_food_per_day_kg = turtle_food_per_day / 1000

total_food_per_day = dog_food_per_day + cat_food_per_day + turtle_food_per_day_kg
food_needed = total_food_per_day * count_days

if left_food >= food_needed:
    print(f"{floor(left_food - food_needed)} kilos of food left.")
else:
    print(f"{ceil(food_needed - left_food)} more kilos of food are needed.")
