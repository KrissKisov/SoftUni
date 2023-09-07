vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
vegetables_weight = int(input())
fruits_weight = int(input())

income = (vegetables_weight * vegetables_price_per_kg + fruits_weight * fruits_price_per_kg) / 1.94

print(f"{income:.2f}")