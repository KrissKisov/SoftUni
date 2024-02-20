class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative

# # input
# 1
# 4
# -5
# 3
# 10

# # output
# Traceback (most recent call last):
#   File ".\value_cannot_be_negative.py", line 8, in <module>
#     raise ValueCannotBeNegative
# __main__.ValueCannotBeNegative
