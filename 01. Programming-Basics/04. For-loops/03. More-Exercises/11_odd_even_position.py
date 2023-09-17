import sys

numbers_count = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for num in range(1, numbers_count + 1):
    current_number = float(input())
    if num % 2 != 0:
        odd_sum += current_number
        if odd_min > current_number:
            odd_min = current_number
        if odd_max < current_number:
            odd_max = current_number
    elif num % 2 == 0:
        even_sum += current_number
        if even_min > current_number:
            even_min = current_number
        if even_max < current_number:
            even_max = current_number
if (odd_min == sys.maxsize or odd_max == -sys.maxsize) \
        and (even_min == sys.maxsize and even_max == -sys.maxsize):
    print(f"OddSum={odd_sum :.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_sum :.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif odd_min == sys.maxsize or odd_max == -sys.maxsize:
    print(f"OddSum={odd_sum :.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_sum :.2f},")
    print(f"EvenMin={even_min :.2f},")
    print(f"EvenMax={even_max :.2f}")
elif even_min == sys.maxsize or even_max == -sys.maxsize:
    print(f"OddSum={odd_sum :.2f},")
    print(f"OddMin={odd_min :.2f},")
    print(f"OddMax={odd_max :.2f},")
    print(f"EvenSum={even_sum :.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"OddSum={odd_sum :.2f},")
    print(f"OddMin={odd_min :.2f},")
    print(f"OddMax={odd_max :.2f},")
    print(f"EvenSum={even_sum :.2f},")
    print(f"EvenMin={even_min :.2f},")
    print(f"EvenMax={even_max :.2f}")

# import sys
#
# numbers_count = int(input())
# odd_sum = 0
# odd_min = sys.maxsize
# odd_max = -sys.maxsize
# even_sum = 0
# even_min = sys.maxsize
# even_max = -sys.maxsize
#
# for num in range(1, numbers_count + 1):
#     current_number = float(input())
#     if num % 2 != 0:
#         odd_sum += current_number
#         odd_min = min(odd_min, current_number)
#         odd_max = max(odd_max, current_number)
#     else:
#         even_sum += current_number
#         even_min = min(even_min, current_number)
#         even_max = max(even_max, current_number)
#
# print(f"OddSum={odd_sum :.2f},")
# print(f"OddMin={'No' if odd_min == sys.maxsize else f'{odd_min:.2f}'},")
# print(f"OddMax={'No' if odd_max == -sys.maxsize else f'{odd_max:.2f}'},")
# print(f"EvenSum={even_sum :.2f},")
# print(f"EvenMin={'No' if even_min == sys.maxsize else f'{even_min:.2f}'},")
# print(f"EvenMax={'No' if even_max == -sys.maxsize else f'{even_max:.2f}'}")
