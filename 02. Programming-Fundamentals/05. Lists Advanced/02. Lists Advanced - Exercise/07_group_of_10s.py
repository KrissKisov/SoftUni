from math import ceil


numbers_list = list(map(int, input().split(", ")))
group = 0
num_groups = ceil(max(numbers_list) / 10)
for current_group in range(1, num_groups + 1):
    group += 10
    temp_list = list(x for x in numbers_list if x <= group)
    print(f"Group of {group}'s: {temp_list}")
    numbers_list = [x for x in numbers_list if x not in temp_list]
