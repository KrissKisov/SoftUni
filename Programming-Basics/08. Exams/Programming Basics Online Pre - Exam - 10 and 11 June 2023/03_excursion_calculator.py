people = int(input())
season = input()  # "spring", "summer", "autumn" или "winter"

price_per_person = 0
if people <= 5:
    if season == "spring":
        price_per_person = 50.00
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60.00
    elif season == "winter":
        price_per_person = 86.00
else:
    if season == "spring":
        price_per_person = 48.00
    elif season == "summer":
        price_per_person = 45.00
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85.00

excursion_price = people * price_per_person
if season == "summer":
    excursion_price *= 0.85
elif season == "winter":
    excursion_price *= 1.08

print(f"{excursion_price :.2f} leva.")
