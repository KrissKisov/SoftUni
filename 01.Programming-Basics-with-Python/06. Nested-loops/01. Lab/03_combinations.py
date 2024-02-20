number = int(input())

combinations = 0
for x_1 in range(number + 1):
    for x_2 in range(number + 1):
        for x_3 in range(number + 1):
            if x_1 + x_2 + x_3 == number:
                combinations += 1
print(combinations)
