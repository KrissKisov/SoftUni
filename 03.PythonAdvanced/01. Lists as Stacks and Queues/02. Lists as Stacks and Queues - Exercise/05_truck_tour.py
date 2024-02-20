from collections import deque

number_of_pumps = int(input())
petrol_stations = deque([int(x) for x in input().split()]for pump in range(number_of_pumps))
petrol_stations_copy = petrol_stations.copy()
amount_in_tank = 0
current_pump_index = 0

while petrol_stations_copy:
    petrol, distance = petrol_stations_copy.popleft()

    amount_in_tank += petrol
    if amount_in_tank >= distance:
        amount_in_tank -= distance
    else:
        petrol_stations.rotate(-1)
        petrol_stations_copy = petrol_stations.copy()
        current_pump_index += 1
        amount_in_tank = 0

print(current_pump_index)
