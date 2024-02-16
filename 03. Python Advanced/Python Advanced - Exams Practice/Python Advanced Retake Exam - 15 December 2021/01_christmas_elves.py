from collections import deque


elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

used_energy = 0
toys = 0
number_of_boxes = 0

while elves and materials:

    current_toy = 1
    current_energy = 0

    elf = elves.popleft()
    if elf < 5:
        continue

    number_of_boxes += 1
    material = materials.pop()

    if number_of_boxes % 3 == 0:

        if elf >= material * 2:
            material *= 2
            current_toy *= 2

        else:
            elf *= 2
            elves.append(elf)
            materials.append(material)
            continue

    if elf < material:
        elf *= 2
        elves.append(elf)
        materials.append(material)
        continue

    elf -= material
    current_energy += material

    elf += 1

    if number_of_boxes % 5 == 0:
        current_toy -= current_toy
        elf -= 1

    toys += current_toy
    used_energy += current_energy

    elves.append(elf)

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")

if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
