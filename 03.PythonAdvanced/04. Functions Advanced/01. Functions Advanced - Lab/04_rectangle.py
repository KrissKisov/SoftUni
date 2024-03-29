# def area(length, width):
#     return length * width
#
#
# def perimeter(length, width):
#     return (length + width) * 2
#
#
# def rectangle(length, width):
#     if not (isinstance(length, (int, float, complex)) and isinstance(width, (int, float, complex))):
#         return "Enter valid values!"
#
#     rectangle_area = area(length, width)
#     rectangle_perimeter = perimeter(length, width)
#
#     return f"Rectangle area: {rectangle_area}\nRectangle perimeter: {rectangle_perimeter}"
#


def rectangle(length, width):
    if not (isinstance(length, (int, float, complex)) and isinstance(width, (int, float, complex))):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# print(rectangle(2, 10))
# print(rectangle('2', 10))
