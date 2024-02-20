decoration_quantity = int(input())
days_to_christmas = int(input())

ornament_set_price = 2
ornament_set_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17
shopping_cost = 0
total_spirit = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        decoration_quantity += 2

    if day % 2 == 0:
        shopping_cost += decoration_quantity * ornament_set_price
        total_spirit += ornament_set_spirit

    if day % 3 == 0:
        shopping_cost += decoration_quantity * (tree_skirt_price + tree_garland_price)
        total_spirit += tree_skirt_spirit + tree_garland_spirit

    if day % 5 == 0:
        shopping_cost += decoration_quantity * tree_lights_price
        total_spirit += tree_lights_spirit

        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        shopping_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_to_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {shopping_cost}")
print(f"Total spirit: {total_spirit}")
