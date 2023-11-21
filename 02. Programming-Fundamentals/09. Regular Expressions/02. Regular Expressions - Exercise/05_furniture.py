import re

total_cost = 0
furniture = []
command = input()
while command != "Purchase":
    pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"  # r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
    match = re.search(pattern, command)
    if match:
        price = float(match.group(2))
        quantity = int(match.group(4))
        furniture.append(match.group(1))
        total_cost += price * quantity

    command = input()
print(f"Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost :.2f}")
