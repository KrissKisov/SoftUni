number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsules = int(input())
    order_price = capsule_price * needed_capsules * days

    # if (not 0.01 <= capsule_price <= 100.00
    #         or not 1 <= days <= 31
    #         or not 1 <= needed_capsules <= 2000):
    #     continue
    if (not 0.01 <= capsule_price <= 100.00
            or days not in range(1, 31 + 1)
            or needed_capsules not in range(1, 2000 + 1)):
        continue
    else:
        print(f"The price for the coffee is: ${order_price :.2f}")
        total_price += order_price

print(f"Total: ${total_price :.2f}")
