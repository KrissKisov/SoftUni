numbers_locations = int(input())

for location in range(numbers_locations):
    expected_mining_per_day = float(input())
    days_per_location = int(input())
    current_mining_per_day = 0
    for mining in range(days_per_location):
        current_day_mining = float(input())
        current_mining_per_day += current_day_mining

    average_mining = current_mining_per_day / days_per_location
    if expected_mining_per_day <= average_mining:
        print(f"Good job! Average gold per day: {average_mining :.2f}.")
    else:
        more_gold_needed = expected_mining_per_day - average_mining
        print(f"You need {more_gold_needed :.2f} gold.")
