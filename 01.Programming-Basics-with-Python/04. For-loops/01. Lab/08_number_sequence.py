import sys

numbers_count = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize
for num in range(numbers_count):
    next_number = int(input())
    if max_number < next_number:
        max_number = next_number
    if min_number > next_number:
        min_number = next_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
