import sys

numbers_count = int(input())
sum_all = 0
biggest_number = -sys.maxsize
for num in range(numbers_count):
    current_number = int(input())
    if current_number > biggest_number:
        biggest_number = current_number
    sum_all += current_number

sum_rest = sum_all - biggest_number
if biggest_number == sum_rest:
    print(f"Yes")
    print(f"Sum = {biggest_number}")
else:
    difference = abs(biggest_number - sum_rest)
    print(f"No")
    print(f"Diff = {difference}")
