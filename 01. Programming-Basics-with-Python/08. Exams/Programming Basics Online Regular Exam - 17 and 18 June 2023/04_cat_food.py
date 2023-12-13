number_of_cats = int(input())
price_per_kg = 12.45
price_per_gram = price_per_kg / 1000
total_food = 0
small_cats_count = 0
big_cats_count = 0
huge_cats_count = 0
for cat in range(number_of_cats):
    current_cat_eats = float(input())
    total_food += current_cat_eats

    if 100 <= current_cat_eats < 200:
        small_cats_count += 1
    elif current_cat_eats < 300:
        big_cats_count += 1
    elif current_cat_eats < 400:
        huge_cats_count += 1

price_per_day = total_food * price_per_gram
print(f"Group 1: {small_cats_count} cats.")
print(f"Group 2: {big_cats_count} cats.")
print(f"Group 3: {huge_cats_count} cats.")
print(f"Price for food per day: {price_per_day :.2f} lv.")
