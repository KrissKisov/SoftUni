##1
# numbers_input = list(map(int, input().split(", ")))
# positive = [str(num) for num in numbers_input if num >= 0]
# negative = [str(num) for num in numbers_input if num < 0]
# even = [str(num) for num in numbers_input if num % 2 == 0]
# odd = [str(num) for num in numbers_input if num % 2 != 0]
# print(f'Positive: {", ".join(positive)}')
# print(f'Negative: {", ".join(negative)}')
# print(f'Even: {", ".join(even)}')
# print(f'Odd: {", ".join(odd)}')

##2
# numbers_input = list(map(int, input().split(", ")))
# print(f"Positive: {', '.join(list(str(num) for num in numbers_input if num >= 0))}")
# print(f"Negative: {', '.join(list(str(num) for num in numbers_input if num < 0))}")
# print(f"Even: {', '.join(list(str(num) for num in numbers_input if num % 2 == 0))}")
# print(f"Odd: {', '.join(list(str(num) for num in numbers_input if num % 2 != 0))}")

##3
numbers_input = input().split(", ")
print(f"Positive: {', '.join(num for num in numbers_input if int(num) >= 0)}")
print(f"Negative: {', '.join(num for num in numbers_input if int(num) < 0)}")
print(f"Even: {', '.join(num for num in numbers_input if int(num) % 2 == 0)}")
print(f"Odd: {', '.join(num for num in numbers_input if int(num) % 2 != 0)}")
