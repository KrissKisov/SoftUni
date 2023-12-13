command = input()
total_price = 0

while command != "special" and command != "regular":
    part_price = float(command)
    if part_price <= 0:
        print("Invalid price!")
        command = input()
        continue
    total_price += part_price
    command = input()

taxes_amount = total_price * 0.2
final_price = total_price + taxes_amount

if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        final_price *= 0.9

    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price :.2f}$\n"
          f"Taxes: {taxes_amount :.2f}$\n"
          f"-----------\n"
          f"Total price: {final_price :.2f}$")
