airline = input()
adult_ticket_number = int(input())
kid_ticket_number = int(input())
adults_price = float(input())
service_fee = float(input())
kids_price = adults_price * 0.3
total_price = adult_ticket_number * (adults_price + service_fee) + kid_ticket_number * (kids_price + service_fee)
profit = total_price * 0.2
print(f"The profit of your agency from {airline} tickets is {profit :.2f} lv.")
