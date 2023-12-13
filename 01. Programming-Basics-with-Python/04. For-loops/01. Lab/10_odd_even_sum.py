numbers_count = int(input())

odd_sum = 0
even_sum = 0
for num in range(numbers_count):
    new_number = int(input())
    if num % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print(f"No")
    print(f"Diff = {diff}")
