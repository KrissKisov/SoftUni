days_of_tournament = int(input())

won_money_per_day = 0
games_won = 0
games_lost = 0
winning_days_count = 0
total_money_won = 0

for day in range(days_of_tournament):
    sport = input()  # "type of sport" or "Finish"

    while sport != "Finish":
        result = input()  # "win" or "lose"
        if result == "win":
            won_money_per_day += 20
            games_won += 1
        else:
            games_lost += 1

        sport = input()

    if games_won > games_lost:
        won_money_per_day *= 1.1
        winning_days_count += 1

    total_money_won += won_money_per_day
    won_money_per_day = 0
    games_won = 0
    games_lost = 0

if days_of_tournament / 2 < winning_days_count:
    total_money_won *= 1.2
    print(f"You won the tournament! Total raised money: {total_money_won :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_won :.2f}")
