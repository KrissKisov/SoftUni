numbers_of_joinery = int(input())
type_joinery = input()  # "90X130" или "100X150" или "130X180" или "200X300"
receiving = input()  # "With delivery" или "Without delivery"

price_small = 110
price_medium = 140
price_large = 190
price_extra_large = 250
current_price = 0
discount = 1

if type_joinery == "90X130":
    if numbers_of_joinery <= 30:
        current_price = price_small * numbers_of_joinery * discount
    elif numbers_of_joinery <= 60:
        discount -= 0.05
        current_price = price_small * numbers_of_joinery * discount
    else:
        discount -= 0.08
        current_price = price_small * numbers_of_joinery * discount
elif type_joinery == "100X150":
    if numbers_of_joinery <= 40:
        current_price = price_medium * numbers_of_joinery * discount
    elif numbers_of_joinery <= 80:
        discount -= 0.06
        current_price = price_medium * numbers_of_joinery * discount
    else:
        discount -= 0.10
        current_price = price_medium * numbers_of_joinery * discount
elif type_joinery == "130X180":
    if numbers_of_joinery <= 20:
        current_price = price_large * numbers_of_joinery * discount
    elif numbers_of_joinery <= 50:
        discount -= 0.07
        current_price = price_large * numbers_of_joinery * discount
    else:
        discount -= 0.12
        current_price = price_large * numbers_of_joinery * discount
else:
    if numbers_of_joinery <= 25:
        current_price = price_extra_large * numbers_of_joinery * discount
    elif numbers_of_joinery <= 50:
        discount -= 0.09
        current_price = price_extra_large * numbers_of_joinery * discount
    else:
        discount -= 0.14
        current_price = price_extra_large * numbers_of_joinery * discount

if receiving == "With delivery":
    current_price += 60

final_price = 0
additional_discount = 1
if numbers_of_joinery <= 10:
    print("Invalid order")
elif numbers_of_joinery <= 99:
    final_price = current_price
    print(f"{final_price :.2f} BGN")
else:
    additional_discount -= 0.04
    final_price = current_price * additional_discount
    print(f"{final_price :.2f} BGN")
