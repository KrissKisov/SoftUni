gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

type_fuel = input()
amount_fuel = float(input())
club_card = input()

discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08

if club_card == "Yes":
    gasoline_price -= discount_gasoline
    diesel_price -= discount_diesel
    gas_price -= discount_gas

if 20 <= amount_fuel <= 25:
    gasoline_price -= gasoline_price * 0.08
    diesel_price -= diesel_price * 0.08
    gas_price -= gas_price * 0.08
elif amount_fuel > 25:
    gasoline_price -= gasoline_price * 0.10
    diesel_price -= diesel_price * 0.10
    gas_price -= gas_price * 0.10

final_price = 0
if type_fuel == "Gasoline":
    final_price = amount_fuel * gasoline_price
elif type_fuel == "Diesel":
    final_price = amount_fuel * diesel_price
elif type_fuel == "Gas":
    final_price = amount_fuel * gas_price

print(f"{final_price:.2f} lv.")
