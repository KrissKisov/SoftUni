month = input()
nights = int(input())

studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.7
        apartment_price *= 0.9
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
else:
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.9

total_stay_studio_price = nights * studio_price
total_stay_apartment_price = nights * apartment_price
print(f"Apartment: {total_stay_apartment_price :.2f} lv.")
print(f"Studio: {total_stay_studio_price :.2f} lv.")
