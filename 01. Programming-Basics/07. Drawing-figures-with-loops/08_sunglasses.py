n = int(input())

for row in range(1, n + 1):
    if row == 1 or row == n:
        print(2 * n * "*" + n * " " + 2 * n * "*")
    else:
        if row == (n - 1) // 2 + 1:
            print("*" + (2 * n - 2) * "/" + "*" + n * "|" + "*" + (2 * n - 2) * "/" + "*")
        else:
            print("*" + (2 * n - 2) * "/" + "*" + n * " " + "*" + (2 * n - 2) * "/" + "*")
