from math import sqrt, floor


def longest_line(first_1, second_1, first_2, second_2):
    first_point = sqrt(first_1 ** 2 + second_1 ** 2)
    second_point = sqrt(first_2 ** 2 + second_2 ** 2)
    return first_point + second_point


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
first_line = longest_line(x1, y1, x2, y2)
second_line = longest_line(x3, y3, x4, y4)

if first_line >= second_line:
    if (x1 ** 2 + y1 ** 2) <= (x2 ** 2 + y2 ** 2):
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
else:
    if (x3 ** 2 + y3 ** 2) <= (x4 ** 2 + y4 ** 2):
        print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
    else:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")
