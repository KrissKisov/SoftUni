amount = float(input())
sex = input()  # 'm' за мъж и 'f' за жена
age = int(input())
sport = input()  # "Gym" "Boxing" "Yoga" "Zumba" "Dances" "Pilates"

price = 0
if sex == "m":
    if sport == "Gym":
        price = 42
    if sport == "Boxing":
        price = 41
    if sport == "Yoga":
        price = 45
    if sport == "Zumba":
        price = 34
    if sport == "Dances":
        price = 51
    if sport == "Pilates":
        price = 39
elif sex == "f":
    if sport == "Gym":
        price = 35
    if sport == "Boxing":
        price = 37
    if sport == "Yoga":
        price = 42
    if sport == "Zumba":
        price = 31
    if sport == "Dances":
        price = 53
    if sport == "Pilates":
        price = 37

if age <= 19:
    price *= 0.8
if amount >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    difference = price - amount
    print(f"You don't have enough money! You need ${difference :.2f} more.")
