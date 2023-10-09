# sequence_of_numbers = input().split()
#
# first_car_total_time = 0
# second_car_total_time = 0
#
# for number in range(len(sequence_of_numbers) // 2):
#     first_car_current_time = int(sequence_of_numbers[number])
#     if first_car_current_time == 0:
#         first_car_total_time *= 0.8
#     first_car_total_time += first_car_current_time
#
# for number in range(len(sequence_of_numbers) - 1, len(sequence_of_numbers) // 2, - 1):
#     second_car_current_time = int(sequence_of_numbers[number])
#     if second_car_current_time == 0:
#         second_car_total_time *= 0.8
#     second_car_total_time += second_car_current_time
#
# winner = ""
# if first_car_total_time < second_car_total_time:
#     winner = "left"
# elif first_car_total_time > second_car_total_time:
#     winner = "right"
#
# print(f"The winner is {winner} with total time: {min(first_car_total_time, second_car_total_time) :.1f}")

sequence_of_numbers = input().split()
first_car_total_time = 0
second_car_total_time = 0
first_car_times = sequence_of_numbers[:len(sequence_of_numbers) // 2]
second_car_times = sequence_of_numbers[-1:len(sequence_of_numbers) // 2: -1]

for time in first_car_times:
    if int(time) == 0:
        first_car_total_time *= 0.8
    first_car_total_time += int(time)

for time in second_car_times:
    if int(time) == 0:
        second_car_total_time *= 0.8
    second_car_total_time += int(time)
if first_car_total_time < second_car_total_time:
    winner = "left"
else:
    winner = "right"

total_time = min(first_car_total_time, second_car_total_time)
print(f"The winner is {winner} with total time: {total_time :.1f}")
