number = int(input())

left_sum = 0
right_sum = 0
for num in range(number * 2):
    current_number = int(input())
    if num < number:
        left_sum += current_number
    else:
        right_sum += current_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
