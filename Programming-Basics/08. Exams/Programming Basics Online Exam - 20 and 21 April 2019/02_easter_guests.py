from math import ceil


num_guest = int(input())
budget = int(input())
easter_bread_price = 4
egg_price = 0.45
num_easter_breads = ceil(num_guest / 3)
num_eggs = num_guest * 2

total_amount = num_easter_breads * easter_bread_price + num_eggs * egg_price

difference = budget - total_amount
if difference >= 0:
    print(f"Lyubo bought {num_easter_breads} Easter bread and {num_eggs} eggs.")
    print(f"He has {difference :.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(difference) :.2f} lv. more.")
