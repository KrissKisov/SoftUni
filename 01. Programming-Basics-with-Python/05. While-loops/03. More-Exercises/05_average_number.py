number = int(input())

total_sum = 0
for num in range(number):
    current_number = int(input())
    total_sum += current_number
average_sum = total_sum / number
print(f"{average_sum:.2f}")
