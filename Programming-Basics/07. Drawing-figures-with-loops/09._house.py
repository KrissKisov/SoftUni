n = int(input())

stars = 0
hyphen = n
for upper_rows in range((n + 1) // 2):
    if n % 2 != 0:
        if upper_rows == 0:
            stars += 1
            hyphen -= 1
            print(hyphen // 2 * "-" + stars * "*" + hyphen // 2 * "-")
        else:
            stars += 2
            hyphen -= 2
            print(hyphen // 2 * "-" + stars * "*" + hyphen // 2 * "-")

    else:
        if upper_rows == 0:
            stars += 2
            hyphen -= 2
            print(hyphen // 2 * "-" + stars * "*" + hyphen // 2 * "-")
        else:
            stars += 2
            hyphen -= 2
            print(hyphen // 2 * "-" + stars * "*" + hyphen // 2 * "-")

for lower_row in range(n // 2):
    print("|" + (n - 2) * "*" + "|")
