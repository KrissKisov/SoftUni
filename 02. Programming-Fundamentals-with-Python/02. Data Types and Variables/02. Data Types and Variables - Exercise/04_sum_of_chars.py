number_of_characters = int(input())
sum_of_char = 0

for char in range(number_of_characters):
    current_character = input()
    sum_of_char += ord(current_character)

print(f"The sum equals: {sum_of_char}")
