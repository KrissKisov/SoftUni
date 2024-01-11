journal = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":
    current_item = command[1]

    if command[0] == "Collect":
        if current_item not in journal:
            journal.append(current_item)

    elif command[0] == "Drop":
        if current_item in journal:
            journal.remove(current_item)

    elif command[0] == "Combine Items":
        old_item, new_item = current_item.split(":")
        if old_item in journal:
            # journal.insert(journal.index(old_item) + 1, new_item)
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index + 1, new_item)

    elif command[0] == "Renew":
        if current_item in journal:
            # journal.append(journal.pop(journal.index(current_item)))
            current_item_index = journal.index(current_item)
            popped_item = journal.pop(current_item_index)
            journal.append(popped_item)

    command = input().split(" - ")

print(", ".join(journal))
