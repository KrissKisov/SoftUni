town = input()  # "Bansko",  "Borovets", "Varna" или "Burgas"
offer_type = input()  # "noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast"
discount = input()  # "yes" или "no"
days = int(input())
price_per_day = 0

if town == "Bansko" or town == "Borovets":

    if offer_type == "withEquipment":
        price_per_day = 100

        if discount == "yes":
            price_per_day *= 0.9

    elif offer_type == "noEquipment":
        price_per_day = 80

        if discount == "yes":
            price_per_day *= 0.95

elif town == "Varna" or town == "Burgas":

    if offer_type == "withBreakfast":
        price_per_day = 130

        if discount == "yes":
            price_per_day *= 0.88

    elif offer_type == "noBreakfast":
        price_per_day = 100

        if discount == "yes":
            price_per_day *= 0.93

total_price = days * price_per_day

if days > 7:
    total_price -= price_per_day

if days < 1:
    print("Days must be positive number!")
elif town != "Bansko" and town != "Borovets" and town != "Varna" and town != "Burgas":
    print("Invalid input!")
elif (offer_type != "noEquipment" and offer_type != "withEquipment"
      and offer_type != "noBreakfast" and offer_type != "withBreakfast"):
    print("Invalid input!")
else:
    print(f"The price is {total_price :.2f}lv! Have a nice time!")
