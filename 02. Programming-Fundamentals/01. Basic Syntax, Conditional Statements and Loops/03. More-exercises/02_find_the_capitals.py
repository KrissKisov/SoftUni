given_string = input()
list_of_indices = []

for index in range(len(given_string)):
    if given_string[index].isupper():
        list_of_indices.append(index)

print(list_of_indices)
