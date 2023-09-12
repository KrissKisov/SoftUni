price_per_page = float(input())
price_per_cover = float(input())
discount = int(input())
designer_price = float(input())
percent_team_paid = int(input())

book_price = price_per_page * 899 + price_per_cover * 2
book_price_discounted = book_price - book_price * discount / 100
final_price = book_price_discounted + designer_price
amount_to_pay = final_price - final_price * percent_team_paid / 100

print(f"Avtonom should pay {amount_to_pay :.2f} BGN.")
