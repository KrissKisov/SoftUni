num_costumers = int(input())
total_spend = 0

for costumer in range(num_costumers):
    command = input()
    count_products = 0
    current_bill = 0

    while command != "Finish":
        product = command  # "basket", "wreath" или "chocolate bunny"
        product_price = 0

        if product == "basket":
            product_price = 1.5
        elif product == "wreath":
            product_price = 3.8
        elif product == "chocolate bunny":
            product_price = 7

        current_bill += product_price
        count_products += 1

        command = input()

    if count_products % 2 == 0:
        current_bill *= 0.8

    total_spend += current_bill

    print(f"You purchased {count_products} items for {current_bill :.2f} leva.")

average_bill = total_spend / num_costumers
print(f"Average bill per client is: {average_bill :.2f} leva.")
