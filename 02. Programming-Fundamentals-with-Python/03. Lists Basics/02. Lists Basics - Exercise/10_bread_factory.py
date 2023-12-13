initial_energy = 100
initial_coins = 100
day_events = input().split("|")
bakery_is_open = True

for event in day_events:
    name, number_as_string = event.split("-")
    number = int(number_as_string)
    if name == "rest":
        if initial_energy + number <= 100:
            gained_energy = number
            initial_energy += number
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif name == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")

        if initial_energy > 100:
            initial_energy = 100

    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
