movie = input()
days = int(input())
num_tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

income = num_tickets * ticket_price * days
profit = income - income * cinema_percent / 100

print(f"The profit from the movie {movie} is {profit :.2f} lv.")
