a1 = int(input())
a2 = int(input())
n = int(input())

for symbol_one in range(a1, a2):
    for symbol_two in range(1, n):
        for symbol_three in range(1, int(n / 2)):
            symbol_four = symbol_one
            if symbol_one % 2 != 0 and (symbol_two + symbol_three + symbol_four) % 2 != 0:
                print(f"{chr(symbol_one)}-{symbol_two}{symbol_three}{symbol_four}")
