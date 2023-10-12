# from math import floor
#
#
# def closest_point(first, second, third, fourth):
#     first_point = first ** 2 + second ** 2
#     # first_point = sqrt(first ** 2 + second ** 2)
#     # second_point = sqrt(third ** 2 + fourth ** 2)
#     second_point = third ** 2 + fourth ** 2
#     if first_point == second_point:
#         return f"({first :.0f}, {second :.0f})"
#     elif first_point < second_point:
#         return f"({first :.0f}, {second :.0f})"
#     else:
#         return f"({third :.0f}, {fourth :.0f})"
#
#
# x1 = floor(float(input()))
# y1 = floor(float(input()))
# x2 = floor(float(input()))
# y2 = floor(float(input()))
# print(closest_point(x1, y1, x2, y2))

from math import floor


def closest_point(first, second, third, fourth):
    first_point = first ** 2 + second ** 2
    second_point = third ** 2 + fourth ** 2
    if first_point == second_point:
        return f"({floor(first)}, {floor(second)})"
    elif first_point < second_point:
        return f"({floor(first)}, {floor(second)})"
    else:
        return f"({floor(third)}, {floor(fourth)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(closest_point(x1, y1, x2, y2))
