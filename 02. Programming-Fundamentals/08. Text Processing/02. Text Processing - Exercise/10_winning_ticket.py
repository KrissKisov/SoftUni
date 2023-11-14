tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']
for current_ticket in tickets:
    ticket = current_ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")

    else:
        left_half = ticket[:10]
        right_half = ticket[10:]
        ticket_is_winning = False
        for winning_symbol in winning_symbols:
            if winning_symbol in left_half and winning_symbol in right_half:
                for number_of_repeating in range(10, 5, -1):
                    if number_of_repeating * winning_symbol in left_half and number_of_repeating * winning_symbol in right_half:
                        if number_of_repeating == 10:
                            print(f'ticket "{ticket}" - {number_of_repeating}{winning_symbol} Jackpot!')
                            ticket_is_winning = True
                            break
                        else:
                            print(f'ticket "{ticket}" - {number_of_repeating}{winning_symbol}')
                            ticket_is_winning = ticket
                            break
            if ticket_is_winning:
                break
        else:
            print(f'ticket "{ticket}" - no match')
