# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.


budget = float(input())
statist = int(input())
costume_price = float(input())

total_costume_price = statist * costume_price
discounted_costume_price = total_costume_price - total_costume_price * 0.1
decor = budget * 0.1
expenses_no_discount= total_costume_price + decor
expenses_with_discount = discounted_costume_price + decor

if statist <= 150:
    if budget < expenses_no_discount:
        print("Not enough money!")
        print(f"Wingard needs {expenses_no_discount - budget:.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {budget - expenses_no_discount:.2f} leva left.")
else:
    if budget < expenses_with_discount:
        print("Not enough money!")
        print(f"Wingard needs {expenses_with_discount - budget:.2f} leva more.")
    else:
        print("Action!")
        print(f"Wingard starts filming with {budget - expenses_with_discount:.2f} leva left.")
