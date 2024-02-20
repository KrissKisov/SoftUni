first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_list = []
for word in first_sequence:
    for string in second_sequence:
        if word in string:
            if word in new_list:
                continue
            new_list.append(word)
            # if word not in new_list:
            #     new_list.append(word)
print(new_list)
