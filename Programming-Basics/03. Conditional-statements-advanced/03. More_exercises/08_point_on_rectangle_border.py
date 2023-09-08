x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

standing_point = ""  # "Border", "Inside / Outside"
if (x == x1 or x == x2) and y1 <= y <= y2:
    standing_point = "Border"
elif x1 <= x <= x2 and (y == y1 or y == y2):
    standing_point = "Border"
else:
    standing_point = "Inside / Outside"
print(standing_point)
