season = input()  # "Spring", "Summer", "Autumn" или "Winter"
km_per_month = float(input())  # kilometers

km_per_season = km_per_month * 4
price_per_km = 0
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        price_per_km = 0.75
    elif km_per_month <= 10000:
        price_per_km = 0.95
    elif km_per_month <= 20000:
        price_per_km = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
        price_per_km = 0.9
    elif km_per_month <= 10000:
        price_per_km = 1.1
    elif km_per_month <= 20000:
        price_per_km = 1.45
else:  # season == "Winter"
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif km_per_month <= 10000:
        price_per_km = 1.25
    elif km_per_month <= 20000:
        price_per_km = 1.45

taxes = 0.1
salary = km_per_season * price_per_km
final_income = salary - salary * taxes

print(f"{final_income :.2f}")
