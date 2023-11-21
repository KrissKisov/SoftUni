import re

total_income = 0
pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)\|[^\|\$\%\.]*(?<=\D)(\d+[\.\d+]*)\$"
command = input()
while command != "end of shift":
    match = re.search(pattern, command)
    if match:
        customer_name, product, count, price = match.groups()
        total_price = int(count) * float(price)
        print(f"{customer_name}: {product} - {total_price :.2f}")
        total_income += total_price

    command = input()

print(f"Total income: {total_income :.2f}")
