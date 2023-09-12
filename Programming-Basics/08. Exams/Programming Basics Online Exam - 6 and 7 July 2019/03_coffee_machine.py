drink = input()  # "Espresso", "Cappuccino" или "Tea"
sugar = input()  # "Without", "Normal" или "Extra"
num_drinks = int(input())
price = 0

if drink == "Espresso":

    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    else:
        price = 1.2

elif drink == "Cappuccino":

    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    else:
        price = 1.6

else:
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    else:
        price = 0.7

total_amount = num_drinks * price

if sugar == "Without":
    total_amount -= total_amount * 35 / 100

if drink == "Espresso" and num_drinks >= 5:
    total_amount -= total_amount * 25 / 100

if total_amount > 15:
    total_amount -= total_amount * 20 / 100

print(f"You bought {num_drinks} cups of {drink} for {total_amount :.2f} lv.")
