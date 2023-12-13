profit_wanted = float(input())
current_profit = 0

while True:
    command = input()
    difference = profit_wanted - current_profit

    if command == "Party!":
        print(f"We need {difference :.2f} leva more.")
        break

    cocktail = command
    num_cocktails = int(input())
    cocktail_price = len(cocktail)
    order_price = num_cocktails * cocktail_price

    if order_price % 2 != 0:
        order_price *= 0.75

    current_profit += order_price

    if current_profit >= profit_wanted:
        print("Target acquired.")
        break

print(f"Club income - {current_profit :.2f} leva.")
