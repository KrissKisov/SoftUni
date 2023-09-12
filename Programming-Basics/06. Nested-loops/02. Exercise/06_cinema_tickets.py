student_ticket = 0
standard_ticket = 0
kid_ticket = 0

command = input()
while command != "Finish":
    available_seats = int(input())
    ticket_type = input()
    total_movie_ticket = 0
    seats_to_sell = available_seats
    while ticket_type != "End":

        if ticket_type == "student":
            student_ticket += 1
            total_movie_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
            total_movie_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
            total_movie_ticket += 1

        seats_to_sell -= 1
        if seats_to_sell <= 0:
            break

        ticket_type = input()
    occupancy_movie = total_movie_ticket / available_seats * 100
    print(F"{command} - {occupancy_movie :.2f}% full.")
    command = input()

total_tickets = student_ticket + standard_ticket + kid_ticket
percent_students = student_ticket / total_tickets * 100
percent_standards = standard_ticket / total_tickets * 100
percent_kids = kid_ticket / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standards :.2f}% standard tickets.")
print(f"{percent_kids :.2f}% kids tickets.")
