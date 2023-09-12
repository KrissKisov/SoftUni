from math import ceil

walls = 4
height = int(input())
width = int(input())
percent_not_to_paint = int(input())
total_area = height * width * walls
area_to_paint = ceil(total_area - total_area * percent_not_to_paint / 100)

command = input()

while command != "Tired!":
    paint_litres = int(command)
    area_to_paint -= paint_litres

    if area_to_paint <= 0:
        break

    command = input()

if area_to_paint < 0:
    print(f"All walls are painted and you have {abs(area_to_paint)} l paint left!")
elif area_to_paint == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{area_to_paint} quadratic m left.")
