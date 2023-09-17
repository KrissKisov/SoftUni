available_space_width = int(input())
available_space_length = int(input())
available_space_height = int(input())

total_boxes_to_fit = available_space_width * available_space_length * available_space_height
command = input()
while command != "Done":
    boxes = int(command)
    total_boxes_to_fit -= boxes
    if total_boxes_to_fit <= 0:
        break
    command = input()

if command == "Done":
    print(f"{total_boxes_to_fit} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_boxes_to_fit)} Cubic meters more.")
