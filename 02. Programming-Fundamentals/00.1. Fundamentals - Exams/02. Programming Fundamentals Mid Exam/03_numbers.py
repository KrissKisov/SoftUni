numbers_list = [int(num) for num in input().split()]
average_value = sum(numbers_list) / len(numbers_list)
bigger_than_average = [x for x in numbers_list if x > average_value]

if len(bigger_than_average) > 0:
    bigger_than_average.sort(reverse=True)
    bigger_than_average = [bigger_than_average[x] for x in range(len(bigger_than_average)) if x < 5]
    print(*bigger_than_average)
else:
    print("No")
