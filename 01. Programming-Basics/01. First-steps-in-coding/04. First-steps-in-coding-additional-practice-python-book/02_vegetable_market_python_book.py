EURO_TO_BGN = 1.94

vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
total_vegetables_in_kg = int(input())
total_fruits_in_kg = int(input())

amount_from_vegetables_in_bgn = total_vegetables_in_kg * vegetables_price_per_kg
amount_from_fruits_in_bgn = total_fruits_in_kg * fruits_price_per_kg
total_amount_in_bgn = amount_from_fruits_in_bgn + amount_from_vegetables_in_bgn
total_amount_in_euro = total_amount_in_bgn / EURO_TO_BGN

if 0.00 <= (vegetables_price_per_kg and fruits_price_per_kg and total_vegetables_in_kg and total_fruits_in_kg) <= 1000.00:
    print(float(total_amount_in_euro))