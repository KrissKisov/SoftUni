products = input().split()
stock = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i + 1])
    stock[key] = value
print(stock)

# products = input().split()
# stock = {products[i]:int(products[i + 1]) for i in range(0, len(products), 2)}
# print(stock)
