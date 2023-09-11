excursion_price = float(input())
available_money = float(input())

total_days = 0
days_in_row_spent = 0
saved_money = 0
while days_in_row_spent < 5:
    action = input()  # "spend" или "save"
    amount_of_money = float(input())
    total_days += 1
    if action == "spend":
        days_in_row_spent += 1
        available_money -= amount_of_money
        if available_money < amount_of_money:
            available_money = 0
        if days_in_row_spent >= 5:
            break
    if action == "save":
        available_money += amount_of_money
        saved_money = available_money
        days_in_row_spent = 0
        if saved_money >= excursion_price:
            break

if days_in_row_spent >= 5:
    print("You can't save the money.")
    print(f"{total_days}")
if saved_money >= excursion_price:
    print(f"You saved the money for {total_days} days.")
