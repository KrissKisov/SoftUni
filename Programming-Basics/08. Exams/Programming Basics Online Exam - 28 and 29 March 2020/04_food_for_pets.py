number_of_days = int(input())
available_food = float(input())

dog_total_food = 0
cat_total_food = 0
day_counter = 0
eaten_food_per_day = 0
biscuits_eaten = 0
total_eaten_food = 0
for day in range(number_of_days):
    dog_eats = int(input())
    cat_eats = int(input())
    day_counter += 1
    dog_total_food += dog_eats
    cat_total_food += cat_eats

    if day_counter == 3:
        day_counter = 0
        biscuits_eaten += (dog_eats + cat_eats) * 0.1

    eaten_food_per_day = dog_eats + cat_eats
    total_eaten_food += eaten_food_per_day

percent_eaten_food = total_eaten_food / available_food * 100
percent_dog_eaten_food = dog_total_food / total_eaten_food * 100
percent_cat_eaten_food = cat_total_food / total_eaten_food * 100

print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{percent_eaten_food :.2f}% of the food has been eaten.")
print(f"{percent_dog_eaten_food :.2f}% eaten from the dog.")
print(f"{percent_cat_eaten_food :.2f}% eaten from the cat.")
