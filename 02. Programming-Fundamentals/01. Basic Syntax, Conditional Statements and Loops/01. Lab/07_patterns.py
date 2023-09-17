number = int(input())

for top_rows in range(1, number +1):
    print(top_rows * "*")
for bottom_rows in range(number - 1, 0, -1):
    print(bottom_rows * "*")
