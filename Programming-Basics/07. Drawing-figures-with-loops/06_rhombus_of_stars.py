n = int(input())

for row in range(1, n + 1):
    print((n - row) * " " + "*" + (row - 1) * " *")

for row in range(2, n + 1):
    print((row - 1) * " " + "*" + (n - row) * " *")
