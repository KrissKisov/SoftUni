budget = float(input())
flour_price_per_kg = float(input())
eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg * 1.25
milk_price_per_bread = milk_price_per_liter / 4
price_for_one_bread = flour_price_per_kg + eggs_price_per_pack + milk_price_per_bread
bread_counter = 0
coloured_eggs_counter = 0

while budget - price_for_one_bread >= 0:
    budget -= price_for_one_bread
    bread_counter += 1
    coloured_eggs_counter += 3

    if bread_counter % 3 == 0:
        coloured_eggs_counter -= (bread_counter - 2)

print(f"You made {bread_counter} loaves of Easter bread! "
      f"Now you have {coloured_eggs_counter} eggs and {budget :.2f}BGN left.")
