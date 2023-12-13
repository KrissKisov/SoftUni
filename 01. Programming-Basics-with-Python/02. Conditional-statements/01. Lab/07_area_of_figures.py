from math import pi

figure = input()

area = 0

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a *  side_b
elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
elif figure == "triangle":
    side = float(input())
    height_to_side = float(input())
    area = side * height_to_side / 2
print(f"{area:.3f}")
