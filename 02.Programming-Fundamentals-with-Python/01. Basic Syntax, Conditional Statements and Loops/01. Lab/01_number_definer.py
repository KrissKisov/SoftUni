# number = float(input())
#
# if number == 0:
#     print("zero")
# elif number < 0:
#     if number < -1_000_000:
#         print("large negative")
#     elif number < -1:
#         print("negative")
#     else:  # -1 < number < 0
#         print("small negative")
# else:  # number > 0
#     if number < 1:
#         print("small positive")
#     elif number < 1_000_000:
#         print("positive")
#     else:  # number > 1_000_000
#         print("large positive")


number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small positive")
    elif number < 1000000:
        print("positive")
    else:
        print("large positive")
else:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) < 1000000:
        print("negative")
    else:
        print("large negative")
