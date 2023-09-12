from math import ceil


people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
parasol_price = float(input())

total_amount = people * entrance_fee + ceil(people / 2) * parasol_price + ceil(people * 0.75) * sunbed_price

print(f"{total_amount :.2f} lv.")
