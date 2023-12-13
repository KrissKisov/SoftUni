budget = float(input())
command = input()
count_product = 0
total_products_price = 0
money_needed = 0
while command != "Stop":
    product_name = command
    product_price = float(input())
    count_product += 1
    if count_product % 3 == 0:
        product_price *= 0.5

    if budget >= product_price:
        budget -= product_price
        total_products_price += product_price
    else:
        money_needed = product_price - budget
        break

    command = input()

if command == "Stop":
    print(f"You bought {count_product} products for {total_products_price :.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {money_needed :.2f} leva!")
