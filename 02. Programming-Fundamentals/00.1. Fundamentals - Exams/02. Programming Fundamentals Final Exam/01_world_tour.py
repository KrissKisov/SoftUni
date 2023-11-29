def add_stop(initial_string, some_index, sub_string) -> str:
    if some_index in range(len(initial_string)):
        initial_string = initial_string[:some_index] + sub_string + initial_stops[some_index:]
        return initial_string
    return initial_string


def remove_stop(initial_string, index_to_start, index_to_end) -> str:
    if index_to_start in range(len(initial_string)) and index_to_end in range(len(initial_string)):
        initial_string = initial_string[:index_to_start] + initial_string[index_to_end + 1:]
        return initial_string
    return initial_string


def switch(initial_string, string_to_remove, replacement_string) -> str:
    if string_to_remove in initial_string:
        initial_string = initial_string.replace(string_to_remove, replacement_string)
        return initial_string
    return initial_string


initial_stops = input()
while True:
    command = input().split(":")
    action = command[0]

    if action == "Travel":
        print(f"Ready for world tour! Planned stops: {initial_stops}")
        break

    elif action == "Add Stop":
        index, string_to_insert = int(command[1]), command[2]
        initial_stops = add_stop(initial_stops, index, string_to_insert)

    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        initial_stops = remove_stop(initial_stops, start_index, end_index)

    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        initial_stops = switch(initial_stops, old_string, new_string)

    print(initial_stops)
