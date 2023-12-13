capacity = int(input())
command = input()
ticket_price = 5
income = 0

while command != "Movie time!":
    people_entering = int(command)

    if capacity < people_entering:
        break

    capacity -= people_entering

    if people_entering % 3 == 0:
        income += people_entering * ticket_price - 5
    else:
        income += people_entering * ticket_price

    command = input()

if command == "Movie time!":
    print(f"There are {capacity} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {income} lv.")
