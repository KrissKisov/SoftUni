from collections import deque

box_of_materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

presents = []
toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while box_of_materials and magic_levels:
    material = box_of_materials.pop() if magic_levels[0] or not box_of_materials[-1] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic:
        continue

    result = material * magic

    if result in toys.keys():
        presents.append(toys[result])
    elif result < 0:
        box_of_materials.append(material + magic)
    elif result > 0:
        box_of_materials.append(material + 15)

presents_set = set(presents)

# if {"Doll", "Wooden train"}.issubset(presents_set) or {"Teddy bear", "Bicycle"}.issubset(presents_set):
if {"Doll", "Wooden train"} <= presents_set or {"Teddy bear", "Bicycle"} <= presents_set:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if box_of_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(box_of_materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for toy in sorted(presents_set):
    print(f"{toy}: {presents.count(toy)}")
