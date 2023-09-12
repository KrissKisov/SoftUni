start_number = int(input())
end_number = int(input())

for current_number in range(start_number, end_number + 1):
    even_sum = 0
    odd_sum = 0
    current_number_as_str = str(current_number)

    # for num, char in enumerate(current_number_as_str):
    for num in range(len(current_number_as_str)):
        if num % 2 == 0:
            # even_sum += int(char)
            even_sum += int(current_number_as_str[num])
        else:
            # odd_sum += int(char)
            odd_sum += int(current_number_as_str[num])

    if even_sum == odd_sum:
        print(current_number, end=" ")
