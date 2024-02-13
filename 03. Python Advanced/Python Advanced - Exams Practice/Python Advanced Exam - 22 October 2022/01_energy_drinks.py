from collections import deque


maximum_caffeine = 300
current_caffeine = 0

caffeine_list = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

while caffeine_list and energy_drinks:

    caffeine = caffeine_list.pop()
    drink = energy_drinks.popleft()
    caffeine_in_drink = caffeine * drink

    if caffeine_in_drink + current_caffeine <= maximum_caffeine:
        current_caffeine += caffeine_in_drink

    else:
        energy_drinks.append(drink)
        current_caffeine -= 30

    if current_caffeine < 0:
        current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
