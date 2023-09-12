strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())
raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

money_strawberries = strawberries_kg * strawberries_price
money_raspberries = raspberries_kg * raspberries_price
money_oranges = oranges_kg * oranges_price
money_bananas = bananas_kg * bananas_price

total_money_needed = money_strawberries + money_raspberries + money_oranges + money_bananas
print(f"{total_money_needed :.2f}")
