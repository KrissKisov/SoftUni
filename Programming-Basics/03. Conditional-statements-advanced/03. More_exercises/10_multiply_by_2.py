while True:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break
    else:
        result = number * 2
        print(f"Result: {result:.2f}")
# while True:
#     number = float(input())
#     if number >= 0:
#         number *= 2
#         print(f"Result: {number:.2f}")
#     else:
#         print(f"Negative number!")
