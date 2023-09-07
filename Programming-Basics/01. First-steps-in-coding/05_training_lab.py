w_hall_length = float(input()) #* 100
h_hall_width = float(input()) #* 100
w_hall_length *= 100
h_hall_width *= 100
corridor = 100
work_space_length = 120
work_space_width = 70
work_space_per_row = (h_hall_width - corridor) // work_space_width
numbers_of_rows = w_hall_length // work_space_length
unusable_work_space = 3
total_work_spaces = int(work_space_per_row * numbers_of_rows - unusable_work_space)

print(total_work_spaces)

# w_hall_length = float(input()) # * 100
# h_hall_width = float(input()) # * 100
# # w_hall_length *= 100
# # h_hall_width *= 100
# corridor = 100
# work_space_length = 120
# work_space_width = 70
# work_space_per_row = (h_hall_width * 100 - corridor) // work_space_width
# numbers_of_rows = w_hall_length * 100 // work_space_length
# unusable_work_space = 3
# total_work_spaces = int(work_space_per_row * numbers_of_rows - unusable_work_space)
#
# if 3 <= h_hall_width <= w_hall_length <= 100:
#     print(total_work_spaces)
# else:
#     print("error")