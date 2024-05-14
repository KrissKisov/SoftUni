from collections import deque


materials_list = input().split()
magic_levels = deque(input().split())

gemstone_sculpture = set()
gold_jewellery = set()
gifts = []

while materials_list and magic_levels:

    material = int(materials_list.pop())
    magic = int(magic_levels.popleft())

    result = material + magic

    if result < 100 and result % 2 == 0:
        result = 2 * material + 3 * magic

    elif result < 100 and result % 2 != 0:
        result *= 2

    elif result > 499:
        result /= 2

    if 100 <= result < 200:
        gifts.append("Gemstone")
        gemstone_sculpture.add("Gemstone")

    elif 200 <= result < 300:
        gifts.append("Porcelain Sculpture")
        gemstone_sculpture.add("Porcelain Sculpture")

    elif 300 <= result < 400:
        gifts.append("Gold")
        gold_jewellery.add("Gold")

    elif 400 <= result < 500:
        gifts.append("Diamond Jewellery")
        gold_jewellery.add("Diamond Jewellery")

gifts_set = set(gifts)

if len(gemstone_sculpture) == 2 or len(gold_jewellery) == 2:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_list:
    print(f"Materials left: {', '.join(materials_list)}")

if magic_levels:
    print(f"Magic left: {', '.join(magic_levels)}")

[print(f"{x}: {gifts.count(x)}") for x in sorted(gifts_set)]
