last_sector = input()
number_of_rows = int(input())
number_of_seats = int(input())
seats_count = 0
for sector in range(65, ord(last_sector) + 1):
    for row in range(1, number_of_rows + 1):
        if row % 2 != 0:
            odd_row_seats = number_of_seats
            for seat in range(97, 97 + odd_row_seats):
                current_sector = chr(sector)
                current_seat = chr(seat)
                seats_count += 1
                print(f"{current_sector}{row}{current_seat}")
        else:
            even_row_seats = number_of_seats + 2
            for seat in range(97, 97 + even_row_seats):
                current_sector = chr(sector)
                current_seat = chr(seat)
                seats_count += 1
                print(f"{current_sector}{row}{current_seat}")
    number_of_rows += 1
print(seats_count)
