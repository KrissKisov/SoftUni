# even_numbers = list(filter(lambda num: num % 2 == 0, map(int, input().split())))

numbers_list = list(map(int, input().split()))
even_numbers = list(filter(lambda num: num % 2 == 0, numbers_list))

print(even_numbers)
