length_of_hall_in_metres = float(input())
width_of_hall_in_metres = float(input())
work_space_length_in_sm = 120
work_space_width_in_sm = 70
corridor_width_in_sm = 100
unusable_work_spaces = 3
work_space_per_row = (width_of_hall_in_metres * 100 - corridor_width_in_sm) // work_space_width_in_sm
number_of_rows = length_of_hall_in_metres * 100 // work_space_length_in_sm
total_work_spaces_in_hall = work_space_per_row * number_of_rows - unusable_work_spaces

if 3 <= width_of_hall_in_metres <= length_of_hall_in_metres <= 100:
    print(int(total_work_spaces_in_hall))