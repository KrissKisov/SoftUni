movie = input()  # "John Wick", "Star Wars" или "Jumanji"
package = input()  # "Drink", "Popcorn" или "Menu"
num_tickets = int(input())

price = 0

if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    else:
        price = 30
else:
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    else:
        price = 14

final_price = num_tickets * price

if movie == "Star Wars" and num_tickets >= 4:
    final_price *= 0.7

if movie == "Jumanji" and num_tickets == 2:
    final_price *= 0.85

print(f"Your bill is {final_price :.2f} leva.")
