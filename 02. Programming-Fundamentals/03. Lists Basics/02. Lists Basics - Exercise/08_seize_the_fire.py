all_fires = input().split("#")
water = int(input())
efforts = 0
extinguished_fire_levels = []

for cell in range(len(all_fires)):
    type_of_fire = all_fires[cell].split(" = ")[0]
    level_of_fire = int(all_fires[cell].split(" = ")[1])
    if type_of_fire == "High":
        if level_of_fire not in range(81, 125 + 1):
            continue
    elif type_of_fire == "Medium":
        if level_of_fire not in range(51, 80 + 1):
            continue
    elif type_of_fire == "Low":
        if level_of_fire not in range(1, 50 + 1):
            continue

    if water >= level_of_fire:
        water -= level_of_fire
        efforts += level_of_fire * 0.25
        extinguished_fire_levels.append(level_of_fire)
    else:
        continue

print(f"Cells:")
for fire in range(len(extinguished_fire_levels)):
    print(f"- {extinguished_fire_levels[fire]}")
print(f"Effort: {efforts :.2f}")
print(f"Total Fire: {sum(extinguished_fire_levels)}")
