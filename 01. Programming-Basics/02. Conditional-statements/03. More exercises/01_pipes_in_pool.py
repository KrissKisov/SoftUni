volume_pool = int(input())
pipe_one_flow = int(input())
pipe_two_flow = int(input())
hours = float(input())

first_pipe = pipe_one_flow * hours
second_pipe = pipe_two_flow * hours
filled_up_water = first_pipe + second_pipe

percent_pipe_one = first_pipe / filled_up_water * 100
percent_pipe_two = second_pipe / filled_up_water * 100
percent_filled_volume = filled_up_water / volume_pool * 100

if filled_up_water <= volume_pool:
    print(f"The pool is {percent_filled_volume:.2f}% full."
          f" Pipe 1: {percent_pipe_one:.2f}%. Pipe 2: {percent_pipe_two:.2f}%.")
else:
    print(f"For {hours} "
           f"hours the pool overflows with {filled_up_water - volume_pool:.2f} liters.")
