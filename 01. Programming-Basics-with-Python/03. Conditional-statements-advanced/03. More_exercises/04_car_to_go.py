budget = float(input())
season = input()  # "Summer" или "Winter"

grade_of_car = ""  # "Economy class", "Compact class" или "Luxury class"
type_of_car = ""  # "Cabrio" и "Jeep".
price = 0
if budget <= 100:
    grade_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.35
    else:
        type_of_car = "Jeep"
        price = budget * 0.65
elif budget <= 500:
    grade_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.45
    else:
        type_of_car = "Jeep"
        price = budget * 0.8
else:
    grade_of_car = "Luxury class"
    type_of_car = "Jeep"
    price = budget * 0.9
print(f"{grade_of_car}")
print(f"{type_of_car} - {price:.2f}")
