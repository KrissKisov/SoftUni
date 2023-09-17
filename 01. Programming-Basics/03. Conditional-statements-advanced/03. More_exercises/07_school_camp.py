season = input()  # “Winter”, “Spring” или “Summer”
group_type = input()  # “boys”, “girls” или “mixed”
students_count = int(input())
nights_count = int(input())

price_per_night = 0
sport = ""
if group_type == "girls":
    if season == "Winter":
        price_per_night = 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.20
        sport = "Athletics"
    else:  # season == "Summer"
        price_per_night = 15
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        price_per_night = 9.60
        sport = "Judo"
    elif season == "Spring":
        price_per_night = 7.20
        sport = "Tennis"
    else:  # season == "Summer"
        price_per_night = 15
        sport = "Football"
else:  # group_type == "mixed"
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.50
        sport = "Cycling"
    else:  # season == "Summer"
        price_per_night = 20
        sport = "Swimming"

discount = 0
if students_count >= 50:
    discount = 0.5
elif students_count >= 20:
    discount = 0.15
elif students_count >= 10:
    discount = 0.05

total_price = students_count * nights_count * price_per_night
final_cost = total_price - total_price * discount
print(f"{sport} {final_cost :.2f} lv.")
