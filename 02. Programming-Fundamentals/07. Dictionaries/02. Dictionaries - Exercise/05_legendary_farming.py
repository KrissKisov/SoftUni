materials_dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_item = ''
item_obtained = False
while True:
    input_line = input().split()
    for i in range(0, len(input_line), 2):
        quantity = int(input_line[i])
        material = input_line[i + 1].lower()
        if material not in materials_dictionary:
            materials_dictionary[material] = 0
        materials_dictionary[material] += quantity

        if material == 'shards' and materials_dictionary[material] >= 250:
            legendary_item = 'Shadowmourne'
            materials_dictionary[material] -= 250
            item_obtained = True
            break
        elif material == 'fragments' and materials_dictionary[material] >= 250:
            legendary_item = 'Valanyr'
            materials_dictionary[material] -= 250
            item_obtained = True
            break
        elif material == 'motes' and materials_dictionary[material] >= 250:
            legendary_item = 'Dragonwrath'
            materials_dictionary[material] -= 250
            item_obtained = True
            break

    if item_obtained:
        break

if item_obtained:
    print(f'{legendary_item} obtained!')
for material, quantity in materials_dictionary.items():
    print(f'{material}: {quantity}')
