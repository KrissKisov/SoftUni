NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
DILUENT_PRICE = 5.00

nylon_needed = int(input())
paint_needed = int(input())
diluent = int(input())
hours_of_work = int(input())

bags = 0.40
total_nylon = nylon_needed + 2
total_paint = paint_needed + (paint_needed * 10 / 100)
expenses = bags + total_nylon * 1.50 + total_paint * 14.50 + diluent * 5.00
price_per_hour = (expenses * 30 / 100) * hours_of_work

final_price = expenses + price_per_hour

print(final_price)