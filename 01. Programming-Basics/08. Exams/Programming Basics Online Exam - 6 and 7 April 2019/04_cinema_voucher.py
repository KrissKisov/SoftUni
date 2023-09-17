voucher_value = int(input())
command = input()
bought_tickets_count = 0
bought_other_products_count = 0
while command != "End":

    purchase = command
    price = 0
    is_movie = False
    is_product = False
    if len(purchase) <= 8:
        is_product = True

        for index in range(len(purchase)):

            if index == 0:
                first_letter = purchase[index]
                first_letter_as_num = ord(first_letter)
                price += first_letter_as_num
            else:
                break

    else:
        is_movie = True

        for index in range(len(purchase)):

            if index == 0:
                first_letter = purchase[index]
                first_letter_as_num = ord(first_letter)
                price += first_letter_as_num

            elif index == 1:
                second_letter = purchase[index]
                second_letter_as_num = ord(second_letter)
                price += second_letter_as_num

            else:
                break

    if voucher_value >= price:
        voucher_value -= price

        if is_movie:
            bought_tickets_count += 1
        elif is_product:
            bought_other_products_count += 1

    else:
        break

    command = input()

print(f"{bought_tickets_count}")
print(f"{bought_other_products_count}")
