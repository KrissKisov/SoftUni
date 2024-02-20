stage_of_tournament = input()  # “Quarter final ”, “Semi final” или “Final”
ticket_type = input()  # “Standard”, “Premium” или “VIP”
num_ticket = int(input())
photo_with_trophy = input()  # 'Y' (yes) или 'N' (no)
ticket_price = 0

if stage_of_tournament == "Quarter final":

    if ticket_type == "Standard":
        ticket_price = 55.50

    elif ticket_type == "Premium":
        ticket_price = 105.20

    else:  # ticket_type == "VIP"
        ticket_price = 118.90

elif stage_of_tournament == "Semi final":

    if ticket_type == "Standard":
        ticket_price = 75.88

    elif ticket_type == "Premium":
        ticket_price = 125.22

    else:  # ticket_type == "VIP"
        ticket_price = 300.40

else:  # stage_of_tournament == "Final"

    if ticket_type == "Standard":
        ticket_price = 110.10

    elif ticket_type == "Premium":
        ticket_price = 160.66

    else:  # ticket_type == "VIP"
        ticket_price = 400

total_price = num_ticket * ticket_price
final_price = 0
if total_price > 4000:
    final_price = total_price * 0.75

elif total_price > 2500:
    final_price = total_price * 0.9

else:
    final_price = total_price

if photo_with_trophy == "Y" and total_price <= 4000:
    final_price += num_ticket * 40

print(f"{final_price :.2f}")
