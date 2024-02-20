expected_amount = int(input())

total_payment_in_cash = 0
payment_in_cash_count = 0
total_payment_with_card = 0
payment_with_card_count = 0
accumulated_amount = 0
payment_count = 1
command = input()
while command != "End":
    product_price = int(command)
    if payment_count % 2 != 0:
        if product_price > 100:
            print("Error in transaction!")
        else:
            total_payment_in_cash += product_price
            payment_in_cash_count += 1
            accumulated_amount += product_price
            print("Product sold!")
    else:
        if product_price < 10:
            print("Error in transaction!")
        else:
            total_payment_with_card += product_price
            payment_with_card_count += 1
            accumulated_amount += product_price
            print("Product sold!")

    if accumulated_amount >= expected_amount:
        break
    payment_count += 1
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")
else:
    average_cash = total_payment_in_cash / payment_in_cash_count
    average_card = total_payment_with_card / payment_with_card_count
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
