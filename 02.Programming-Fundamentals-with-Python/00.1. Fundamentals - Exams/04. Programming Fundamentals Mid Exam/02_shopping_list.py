initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    if "Urgent" in command:
        item_to_add = command.split()[1]
        if item_to_add not in initial_list:
            initial_list.insert(0, item_to_add)

    elif "Unnecessary" in command:
        item_to_remove = command.split()[1]
        if item_to_remove in initial_list:
            initial_list.remove(item_to_remove)

    elif "Correct" in command:
        old_item = command.split()[1]
        new_item = command.split()[2]
        if old_item in initial_list:
            index_to_insert = initial_list.index(old_item)
            initial_list.remove(old_item)
            initial_list.insert(index_to_insert, new_item)

    elif "Rearrange" in command:
        item_to_rearrange = command.split()[1]
        if item_to_rearrange in initial_list:
            initial_list.append(initial_list.pop(initial_list.index(item_to_rearrange)))

    command = input()

print(", ".join(initial_list))
