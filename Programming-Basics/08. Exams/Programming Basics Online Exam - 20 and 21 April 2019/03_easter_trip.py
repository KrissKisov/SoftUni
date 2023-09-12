destination = input()  # "France", "Italy" или "Germany"
dates = input()  # "21-23", "24-27" или "28-31"
num_nights = int(input())
price_per_night = 0

if destination == "France":
    if dates == "21-23":
        price_per_night = 30
    elif dates == "24-27":
        price_per_night = 35
    else:
        price_per_night = 40
elif destination == "Italy":
    if dates == "21-23":
        price_per_night = 28
    elif dates == "24-27":
        price_per_night = 32
    else:
        price_per_night = 39
else:
    if dates == "21-23":
        price_per_night = 32
    elif dates == "24-27":
        price_per_night = 37
    else:
        price_per_night = 43

total_cost = num_nights * price_per_night
print(f"Easter trip to {destination} : {total_cost :.2f} leva.")
