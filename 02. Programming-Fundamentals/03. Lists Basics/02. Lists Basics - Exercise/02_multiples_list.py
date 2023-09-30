factor = int(input())
count = int(input())
multiples_list = []
for number in range(1, count + 1):
    multiples_list.append(number * factor)

print(multiples_list)
