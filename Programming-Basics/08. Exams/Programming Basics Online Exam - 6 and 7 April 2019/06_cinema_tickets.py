command = input()
total_tickets = 0
count_students = 0
count_standards = 0
count_kids = 0
while command != "Finish":
    available_seats = int(input())
    movie = command
    ticket_type = input()
    tickets_to_sell = available_seats
    sold_tickets = 0

    while ticket_type != "End":
        if ticket_type == "student":
            count_students += 1
        elif ticket_type == "standard":
            count_standards += 1
        elif ticket_type == "kid":
            count_kids += 1

        sold_tickets += 1
        total_tickets += 1
        available_seats -= 1
        if available_seats <= 0:
            break

        ticket_type = input()

    occupancy = sold_tickets / tickets_to_sell * 100
    print(f"{movie} - {occupancy :.2f}% full.")

    command = input()

percent_students = count_students / total_tickets * 100
percent_standards = count_standards / total_tickets * 100
percent_kids = count_kids / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standards :.2f}% standard tickets.")
print(f"{percent_kids :.2f}% kids tickets.")
