products = input().split()
searched_product = input().split()
stock = {}
for i in range(0, len(products), 2):
    product = products[i]
    quantity = products[i + 1]
    stock[product] = int(quantity)

for element in searched_product:
    if element in stock:
        print(f"We have {stock[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
