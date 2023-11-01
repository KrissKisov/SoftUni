stock = {}
command = input()
while command != "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product not in stock:
        stock[product] = 0
    stock[product] += quantity
    command = input()

print(f"Products in stock:")
for key in stock:
    print(f"- {key}: {stock[key]}")
# for (product, quantity) in stock.items():
#     print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
