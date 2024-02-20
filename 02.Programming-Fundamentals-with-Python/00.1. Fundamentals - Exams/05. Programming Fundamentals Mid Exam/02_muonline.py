health = 100
bitcoins = 0
dungeon_rooms = input().split("|")
room_number = 0

for room in dungeon_rooms:
    room_number += 1
    command = room.split()[0]
    number = int(room.split()[1])

    if command == "potion":
        amount_to_heal = 100 - health
        if number <= amount_to_heal:
            health += number
        else:
            health += amount_to_heal

        print(f"You healed for {min(number, amount_to_heal)} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
