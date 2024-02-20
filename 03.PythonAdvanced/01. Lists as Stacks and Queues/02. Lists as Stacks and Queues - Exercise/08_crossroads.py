from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()

command = input()
num_of_cars_pass = 0
crash_happen = False

while command != "END":

    if command == "green":
        time = green_light

        while time > 0 and cars:
            current_car = cars.popleft()

            if time >= len(current_car):
                time -= len(current_car)
                num_of_cars_pass += 1

                if time > 0 and cars:
                    continue

            else:
                time += free_window

                if len(current_car) > time:
                    crash_at = time
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[crash_at]}.")
                    crash_happen = True
                    break

                else:
                    num_of_cars_pass += 1
                    time = 0
                    continue

    else:
        cars.append(command)

    if crash_happen:
        break

    command = input()

if not crash_happen:
    print("Everyone is safe.")
    print(f"{num_of_cars_pass} total cars passed the crossroads.")
