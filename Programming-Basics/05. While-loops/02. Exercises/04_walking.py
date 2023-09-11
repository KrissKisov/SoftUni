# steps_to_do = 10000
#
# steps_done = 0
# command = input()
# while command != "Going home":
#     current_steps = int(command)
#     steps_done += current_steps
#     if steps_done >= steps_to_do:
#         break
#     command = input()
#
# if command == "Going home":
#     command = input()
#     current_steps = int(command)
#     steps_done += current_steps
#
# if steps_done >= steps_to_do:
#     print("Goal reached! Good job!")
#     print(f"{steps_done - steps_to_do} steps over the goal!")
# else:
#     print(f"{steps_to_do - steps_done} more steps to reach goal.")

#    # The above code is working too.

steps_to_do = 10000

steps_done = 0
while steps_done < steps_to_do:
    command = input()
    if command == "Going home":
        command = input()
        current_steps = int(command)
        steps_done += current_steps
        break
    current_steps = int(command)
    steps_done += current_steps

if steps_done >= steps_to_do:
    print("Goal reached! Good job!")
    print(f"{steps_done - steps_to_do} steps over the goal!")
else:
    print(f"{steps_to_do - steps_done} more steps to reach goal.")
