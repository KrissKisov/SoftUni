screening_type = input()
row_count = int(input())
column_count = int(input())

premiere = 12
normal = 7.50
discounted = 5

price = 0
if screening_type == 'Premiere':
    price = premiere
elif screening_type == 'Normal':
    price = normal
elif screening_type == 'Discount':
    price = discounted

income = row_count * column_count * price
print(f'{income:.2f} leva')
