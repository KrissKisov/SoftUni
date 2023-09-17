from math import floor, ceil

vineyard_area = int(input())
grape_per_sq_meter = float(input())
liters_wine_wanted = int(input())
count_workers = int(input())

total_grape = grape_per_sq_meter * vineyard_area
grape_to_use = total_grape * 40 / 100
total_wine = grape_to_use / 2.5

if total_wine < liters_wine_wanted:
    print(f"It will be a tough winter! More {floor(liters_wine_wanted - total_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(total_wine - liters_wine_wanted)} liters left -> {ceil((total_wine - liters_wine_wanted) / count_workers)} liters per person.")
