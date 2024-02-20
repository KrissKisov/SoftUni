# def lift_capacity(the_lift: list, people: int) -> list:
#     for wagon in range(len(the_lift)):
#         current_wagon = the_lift[wagon]
#         if current_wagon < 4:
#             free_spaces = max_people_in_wagon - current_wagon
#             current_wagon += free_spaces
#             the_lift[wagon] = current_wagon
#             people -= free_spaces
#     return the_lift


waiting_people = int(input())
lift = list(map(int, input().split()))
max_people_in_wagon = 4
for wagon in range(len(lift)):
    current_wagon = lift[wagon]
    if current_wagon < 4:
        free_spaces = max_people_in_wagon - current_wagon
        if free_spaces <= waiting_people:
            current_wagon += free_spaces
            lift[wagon] = current_wagon
            waiting_people -= free_spaces
        else:
            current_wagon += waiting_people
            lift[wagon] = current_wagon
            waiting_people -= waiting_people
            break

the_lift_is_full = True
for wagon in lift:
    if wagon < 4:
        the_lift_is_full = False
        break

lift = map(str, lift)
if waiting_people == 0 and the_lift_is_full:
    print(" ".join(lift))
elif waiting_people == 0 and not the_lift_is_full:
    print(f"The lift has empty spots!\n"
          f"{' '.join(lift)}")
elif waiting_people > 0 and the_lift_is_full:
    print(f"There isn't enough space! {waiting_people} people in a queue!\n"
          f"{' '.join(lift)}")
