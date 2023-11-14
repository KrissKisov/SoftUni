start_char = input()
end_char = input()
random_string = input()
total_sum = 0
for character in random_string:
    if ord(character) in range(ord(start_char) + 1, ord(end_char)):
        total_sum += ord(character)

print(total_sum)
