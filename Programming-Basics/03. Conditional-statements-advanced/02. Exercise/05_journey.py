budget = float(input())
season = input()

destination =""
vacation_cost = 0
type_of_stay = ""
if budget <= 100:
	destination = "Bulgaria"
	if season == "summer":
		vacation_cost = budget * 0.3
		type_of_stay = "Camp"
	elif season == "winter":
		vacation_cost = budget * 0.7
		type_of_stay = "Hotel"
elif budget <= 1000:
	destination = "Balkans"
	if season == "summer":
		vacation_cost = budget * 0.4
		type_of_stay = "Camp"
	elif season == "winter":
		vacation_cost = budget * 0.8
		type_of_stay = "Hotel"
else:
	destination = "Europe"
	vacation_cost = budget * 0.9
	type_of_stay = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_stay} - {vacation_cost :.2f}")
