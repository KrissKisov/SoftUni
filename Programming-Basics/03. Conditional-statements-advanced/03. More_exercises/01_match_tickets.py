VIP = 499.99
Normal = 249.99

budget = float(input())
category = input()
numbers_fans = int(input())

transport = 0
if numbers_fans <= 4:
    transport = budget * 0.75
elif numbers_fans <= 9:
    transport = budget * 0.60
elif numbers_fans <= 24:
    transport = budget * 0.50
elif numbers_fans <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25

tickets_amount = 0
if category == "VIP":
    tickets_amount = numbers_fans * VIP
elif category == "Normal":
    tickets_amount = numbers_fans * Normal

money_for_tickets = budget - transport
if money_for_tickets >= tickets_amount:
    print(f"Yes! You have {money_for_tickets - tickets_amount:.2f} leva left.")
else:
    print(f"Not enough money! You need {tickets_amount - money_for_tickets:.2f} leva.")
