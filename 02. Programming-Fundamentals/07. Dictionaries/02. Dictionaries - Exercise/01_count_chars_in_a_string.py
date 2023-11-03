string = input()
characters_count = {}

for char in string:
    if char == ' ':
        continue

    if char not in characters_count:
        characters_count[char] = 0
    characters_count[char] += 1

for char, number in characters_count.items():
    print(f'{char} -> {number}')
