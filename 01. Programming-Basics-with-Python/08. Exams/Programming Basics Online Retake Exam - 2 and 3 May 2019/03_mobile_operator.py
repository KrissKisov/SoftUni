contract_length = input()  # "one", или "two"
type_contract = input()  # "Small",  "Middle", "Large"или "ExtraLarge"
mobile_internet = input()  # "yes" или "no"
num_months = int(input())
price = 0
discount_for_two_years = 3.75 / 100
if type_contract == "Small":
    if contract_length == "one":
        price = 9.98
    else:
        price = 8.58
elif type_contract == "Middle":
    if contract_length == "one":
        price = 18.99
    else:
        price = 17.09
elif type_contract == "Large":
    if contract_length == "one":
        price = 25.98
    else:
        price = 23.59
else:
    if contract_length == "one":
        price = 35.99
    else:
        price = 31.79

if mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total_price = price * num_months
if contract_length == "two":
    total_price -= total_price * discount_for_two_years

print(f"{total_price :.2f} lv.")
