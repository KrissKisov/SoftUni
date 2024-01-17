from collections import deque

expression = deque(input().split())
integers = deque()

action = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a // b,
}

while len(expression) > 0:
    symbol = expression.popleft()

    if symbol not in "*+-/":
        integers.append(int(symbol))

    else:
        result = 0
        while len(integers) > 1:
            first = integers.popleft()
            second = integers.popleft()
            result = action[symbol](first, second)
            integers.appendleft(result)
            continue
        else:
            expression.appendleft(str(result))
            integers.popleft()

print(*integers)

# from collections import deque
# from math import floor
#
# expression = deque(input().split())  # [6, 5, -, 4, 5, +]
#
# idx = 0
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element in "/*+-":
#         for _ in range(idx - 1):
#             expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))
#
#         del expression[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))
