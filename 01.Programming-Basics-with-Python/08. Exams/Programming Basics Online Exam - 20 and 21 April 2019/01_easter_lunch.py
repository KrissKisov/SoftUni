num_easter_breads = int(input())
dozens_of_eggs = int(input())
cookies_kg = int(input())
easter_bread_price = 3.20
dozens_of_eggs_price = 4.35
cookies_price_kg = 5.40
paint_per_egg_price = 0.15

total_amount = (num_easter_breads * easter_bread_price + dozens_of_eggs * dozens_of_eggs_price
                + cookies_kg * cookies_price_kg + dozens_of_eggs * 12 * paint_per_egg_price)
print(f"{total_amount :.2f}")
