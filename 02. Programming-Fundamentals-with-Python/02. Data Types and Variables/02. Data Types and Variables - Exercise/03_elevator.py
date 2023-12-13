number_of_people = int(input())
capacity_of_elevator = int(input())
minimum_trips = number_of_people // capacity_of_elevator
total_trips = 0

if number_of_people % capacity_of_elevator == 0:
    total_trips = minimum_trips
else:
    total_trips = minimum_trips + 1

print(total_trips)

# from math import ceil
#
# persons = int(input())
# capacity = int(input())
# courses = ceil(persons / capacity)
# print(courses)
