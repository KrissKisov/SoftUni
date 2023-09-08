budget = float(input())
season = input()  # "Summer" или "Winter"

location = ""  # "Alaska" и "Morocco"
staying_in = ""  # "Hotel", "Hut" или "Camp"
price = 0
if budget <= 1000:
    staying_in = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:  # season == "Winter"
        location = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    staying_in = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    else:  # season == "Winter"
        location = "Morocco"
        price = budget * 0.6
else:  # budget > 3000
    staying_in = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:  # season == "Winter"
        location = "Morocco"

print(f"{location} - {staying_in} - {price :.2f}")
