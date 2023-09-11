count_of_numbers = int(input())

first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
fifth_group = 0
for num in range(count_of_numbers):
    number = int(input())
    if number < 200:
        first_group += 1
    elif number < 400:
        second_group += 1
    elif number < 600:
        third_group += 1
    elif number < 800:
        fourth_group += 1
    else:
        fifth_group += 1

first_group_in_percent = first_group / count_of_numbers * 100
second_group_in_percent = second_group / count_of_numbers * 100
third_group_in_percent = third_group / count_of_numbers * 100
fourth_group_in_percent = fourth_group / count_of_numbers * 100
fifth_group_in_percent = fifth_group / count_of_numbers * 100

print(f"{first_group_in_percent:.2f}%")
print(f"{second_group_in_percent:.2f}%")
print(f"{third_group_in_percent:.2f}%")
print(f"{fourth_group_in_percent:.2f}%")
print(f"{fifth_group_in_percent:.2f}%")
