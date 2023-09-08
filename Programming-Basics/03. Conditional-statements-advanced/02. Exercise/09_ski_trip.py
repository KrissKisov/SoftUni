days_of_stay = int(input())
type_of_stay = input()  # "room for one person", "apartment" или "president apartment"
review = input()  # "positive" (-25%)  или "negative" (-10%)

price_room_for_one_person = 18
price_apartment = 25
price_president_apartment = 35
nights_of_stay = days_of_stay - 1
discount = 0
price = 0
if type_of_stay == "apartment":
    if days_of_stay < 10:
        discount = 0.3
    elif days_of_stay < 15:
        discount = 0.35
    else:
        discount = 0.5
    price = nights_of_stay * price_apartment * (1 - discount)
elif type_of_stay == "president apartment":
    if days_of_stay < 10:
        discount = 0.1
    elif days_of_stay < 15:
        discount = 0.15
    else:
        discount = 0.2
    price = nights_of_stay * price_president_apartment * (1 - discount)
else:
    price = nights_of_stay * price_room_for_one_person

if review == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f"{price :.2f}")
