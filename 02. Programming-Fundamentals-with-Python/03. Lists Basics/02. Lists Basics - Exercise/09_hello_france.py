train_ticket = 150
items_with_prices = input().split("|")
budget = float(input())
bought_item_prices = []
spent_money = 0
earned_money = 0

for item in items_with_prices:
    type_of_item, price_as_string = item.split("->")
    price_as_float = float(price_as_string)
    if type_of_item == "Clothes" and price_as_float > 50.00:
        continue
    elif type_of_item == "Shoes" and price_as_float > 35.00:
        continue
    elif type_of_item == "Accessories" and price_as_float > 20.50:
        continue
    else:
        if budget < price_as_float:
            continue
        else:
            budget -= price_as_float
            spent_money += price_as_float
            bought_item_prices.append(price_as_float)

bought_item_new_prices = []
for price in bought_item_prices:
    selling_price = price * 1.4
    earned_money += selling_price
    budget += selling_price
    bought_item_new_prices.append(selling_price)

profit = earned_money - spent_money
for new_price in bought_item_new_prices:
    print(f"{new_price :.2f}", end=" ")
print()
print(f"Profit: {profit :.2f}")
if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
