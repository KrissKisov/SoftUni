from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    keys_queue = deque(kwargs.keys())

    while numbers:
        number = numbers.popleft()
        while keys_queue:
            key = keys_queue.popleft()
            if key == "a":
                kwargs[key] += number

            elif key == "s":
                kwargs[key] -= number

            elif key == "d":
                if number != 0:
                    kwargs[key] /= number

            elif key == "m":
                kwargs[key] *= number

            keys_queue.append(key)
            break

        if not numbers:
            break

    kwargs = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])))

    return '\n'.join(f"{k}: {v :.1f}" for k, v in kwargs.items())

# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print()
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print()
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
#
# def math_operations(*numbers, **kwargs):
#     keys = list(kwargs.keys())  # [a, s, d, m]
#
#     for i in range(len(numbers)):
#         key = keys[i % 4]  # 0, 1, 2, 3
#
#         if key == "a":
#             kwargs[key] += numbers[i]
#         elif key == "s":
#             kwargs[key] -= numbers[i]
#         elif key == "d":
#             if numbers[i] != 0:
#                 kwargs[key] /= numbers[i]
#         elif key == "m":
#             kwargs[key] *= numbers[i]
#
#     kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#
#     return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)
