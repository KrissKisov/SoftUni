starting_list = input().split()
number_to_execute = int(input())
order_of_execution = []
starting_position = 0

while len(starting_list) > 0:
    starting_position = (starting_position + number_to_execute - 1) % len(starting_list)
    removed_number = starting_list.pop(starting_position)
    order_of_execution.append(removed_number)

print(f"[{','.join(order_of_execution)}]")
