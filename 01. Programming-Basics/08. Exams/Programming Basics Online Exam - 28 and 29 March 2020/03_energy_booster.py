fruit = input()  # "Watermelon", "Mango", "Pineapple" или "Raspberry"
set_size = input()  # "small" или "big"
sets_ordered = int(input())
boosters_in_set = 0
booster_price = 0
if fruit == "Watermelon":
    if set_size == "small":
        booster_price = 56
        boosters_in_set = 2
    elif set_size == "big":
        booster_price = 28.70
        boosters_in_set = 5
elif fruit == "Mango":
    if set_size == "small":
        booster_price = 36.66
        boosters_in_set = 2
    elif set_size == "big":
        booster_price = 19.60
        boosters_in_set = 5
elif fruit == "Pineapple":
    if set_size == "small":
        booster_price = 42.10
        boosters_in_set = 2
    elif set_size == "big":
        booster_price = 24.80
        boosters_in_set = 5
elif fruit == "Raspberry":
    if set_size == "small":
        booster_price = 20
        boosters_in_set = 2
    elif set_size == "big":
        booster_price = 15.20
        boosters_in_set = 5

total_price = sets_ordered * boosters_in_set * booster_price
amount_to_pay = 0
if total_price < 400:
    amount_to_pay = total_price
elif total_price <= 1000:
    amount_to_pay = total_price * 0.85
else:
    amount_to_pay = total_price * 0.5

print(f"{amount_to_pay :.2f} lv.")
