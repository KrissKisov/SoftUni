from collections import deque


SEQUENCES_LENGTH = 4

initial_fuel_list = [int(x) for x in input().split()]
consumption_indexes_list = deque(int(x) for x in input().split())
needed_fuel_list = deque(int(x) for x in input().split())

reached_altitude = []

for i in range(1, SEQUENCES_LENGTH + 1):

    fuel = initial_fuel_list.pop()
    consumption = consumption_indexes_list.popleft()
    needed_fuel = needed_fuel_list.popleft()

    result = fuel - consumption
    current_altitude = f"Altitude {i}"
    if result >= needed_fuel:
        reached_altitude.append(current_altitude)
        print(f"John has reached: {current_altitude}")

    else:
        print(f"John did not reach: {current_altitude}")
        break

if not reached_altitude:
    print("John failed to reach the top.\n"
          "John didn't reach any altitude.")

elif len(reached_altitude) < SEQUENCES_LENGTH:
    print(f"John failed to reach the top.\n"
          f"Reached altitudes: {', '.join(reached_altitude)}")

else:
    print("John has reached all the altitudes and managed to reach the top!")
