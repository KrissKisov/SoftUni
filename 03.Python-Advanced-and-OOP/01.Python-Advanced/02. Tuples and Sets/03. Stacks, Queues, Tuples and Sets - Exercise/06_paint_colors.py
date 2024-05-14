from collections import deque

substrings = deque(input().split())

possible_colours = ("red", "yellow", "blue", "orange", "purple", "green")
main_colors = ("red", "yellow", "blue")
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
colours = []

while substrings:
    first_string = substrings.popleft()
    second_string = substrings.pop() if substrings else ""
    result = (first_string + second_string, second_string + first_string)

    for colour in result:
        if colour in possible_colours:
            colours.append(colour)
            break
    else:
        for string_to_insert in (first_string[:-1], second_string[:-1]):
            if string_to_insert:
                substrings.insert(len(substrings) // 2, string_to_insert)

for colour in set(secondary_colors.keys()).intersection(colours):
    if not secondary_colors[colour].issubset(colours):
        colours.remove(colour)

print(colours)
