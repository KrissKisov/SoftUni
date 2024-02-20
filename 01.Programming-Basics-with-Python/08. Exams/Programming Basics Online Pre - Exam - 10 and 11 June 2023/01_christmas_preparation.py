wrapping_paper_price = 5.80
fabric_price = 7.20
glue_price_per_liter = 1.20

wrapping_paper_count = int(input())
fabric_count = int(input())
glue_litres = float(input())
discount = int(input())

amount_wrapping_paper = wrapping_paper_count * wrapping_paper_price
amount_fabric = fabric_count * fabric_price
amount_glue = glue_litres * glue_price_per_liter
total_amount = amount_wrapping_paper + amount_fabric + amount_glue
total_amount_with_discount = total_amount - total_amount * discount / 100

print(f"{total_amount_with_discount :.3f}")
