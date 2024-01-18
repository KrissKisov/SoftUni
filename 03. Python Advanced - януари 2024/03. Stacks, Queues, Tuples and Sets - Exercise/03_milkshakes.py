from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)

    elif milk <= 0:
        chocolates.append(chocolate)

    elif chocolate == milk:
        milkshakes += 1

    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes < 5:
    print('Not enough milkshakes.')
else:
    print('Great! You made all the chocolate milkshakes needed!')

if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f'Milk: {", ".join(str(x) for x in cups_of_milk)}')
else:
    print('Milk: empty')
