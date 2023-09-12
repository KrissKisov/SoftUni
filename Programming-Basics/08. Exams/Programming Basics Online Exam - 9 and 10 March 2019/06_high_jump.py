aim_height = int(input())
start_height = aim_height - 30
number_of_jumps = 0
is_aim_reached = False

while not is_aim_reached:

    is_jump_successful = False

    for jump in range(3):
        number_of_jumps += 1
        current_height = int(input())

        if current_height > start_height:
            is_jump_successful = True
            break

    if start_height >= aim_height and is_jump_successful:
        is_aim_reached = True
        break

    if is_jump_successful:
        start_height += 5
    else:
        break

if is_aim_reached:
    print(f"Tihomir succeeded, he jumped over {start_height}cm "
          f"after {number_of_jumps} jumps.")
else:
    print(f"Tihomir failed at {start_height}cm "
          f"after {number_of_jumps} jumps.")
