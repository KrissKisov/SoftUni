degrees = int(input())
time_day_night = input()

outfit = ''
shoes = ''
if 10 <= degrees <= 18:
    if time_day_night == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time_day_night == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif time_day_night == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees <= 24:
    if time_day_night == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif time_day_night == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif time_day_night == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degrees >= 25:
    if time_day_night == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif time_day_night == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif time_day_night == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
