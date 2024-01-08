neighborhood = list(map(int, input().split("@")))
command = input().split()
starting_house = 0

while "Love!" not in command:
    jump_length = int(command[1])
    house_to_get_hearts = starting_house + jump_length
    if house_to_get_hearts <= len(neighborhood) - 1:
        if neighborhood[house_to_get_hearts] == 0:
            print(f"Place {house_to_get_hearts} already had Valentine's day.")
        elif neighborhood[house_to_get_hearts] == 2:
            neighborhood[house_to_get_hearts] -= 2
            print(f"Place {house_to_get_hearts} has Valentine's day.")
        else:
            neighborhood[house_to_get_hearts] -= 2
    else:
        house_to_get_hearts = 0
        if neighborhood[house_to_get_hearts] == 0:
            print(f"Place {house_to_get_hearts} already had Valentine's day.")
        elif neighborhood[house_to_get_hearts] == 2:
            neighborhood[house_to_get_hearts] -= 2
            print(f"Place {house_to_get_hearts} has Valentine's day.")
        else:
            neighborhood[house_to_get_hearts] -= 2

    starting_house = house_to_get_hearts

    command = input().split()

print(f"Cupid's last position was {starting_house}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    complete_houses_count = neighborhood.count(0)
    incomplete_houses_count = len(neighborhood) - complete_houses_count
    print(f"Cupid has failed {incomplete_houses_count} places.")
