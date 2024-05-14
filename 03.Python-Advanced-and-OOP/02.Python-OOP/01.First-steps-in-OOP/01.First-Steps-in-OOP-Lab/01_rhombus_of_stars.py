def create_top_half(num: int):
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)


def create_bottom_half(num: int):
    for row in range(n - 1, 0, -1):
        print(" " * (n - row) + "* " * row)


def create_rhombus(number: int):
    create_top_half(number)
    create_bottom_half(number)


n = int(input())

create_rhombus(n)
