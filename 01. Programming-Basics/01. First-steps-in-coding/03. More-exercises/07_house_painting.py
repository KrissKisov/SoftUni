x = float(input())
y = float(input())
h = float(input())

door_area = 1.2 * 2
front_back_walls = (x * x) * 2 - door_area
windows_area = 1.5 * 1.5 * 2
side_walls = (x * y) * 2 - windows_area
roof_sides_area = x * y * 2
roof_front_back_area = (x * h * 0.5) * 2

green_paint = (front_back_walls + side_walls) / 3.4
red_paint = (roof_sides_area + roof_front_back_area) / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")