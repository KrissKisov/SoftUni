given_string = input()
output = ""
explosion_power = 0

for index, char in enumerate(given_string):
    if explosion_power > 0 and char != ">":
        explosion_power -= 1
    elif char != ">":
        output += char
    elif char == ">":
        output += char
        explosion_power += int(given_string[index + 1])

print(output)
