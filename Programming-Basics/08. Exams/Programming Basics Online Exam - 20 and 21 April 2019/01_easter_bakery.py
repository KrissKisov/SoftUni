price_flour_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
pack_of_eggs = int(input())
pack_of_yeast = int(input())
price_sugar_kg = price_flour_kg * 0.75
price_pack_eggs = price_flour_kg * 1.1
price_pack_yeast = price_sugar_kg * 0.2

total_amount = (flour_kg * price_flour_kg + sugar_kg * price_sugar_kg
                + pack_of_eggs * price_pack_eggs + pack_of_yeast * price_pack_yeast)

print(f"{total_amount :.2f}")
