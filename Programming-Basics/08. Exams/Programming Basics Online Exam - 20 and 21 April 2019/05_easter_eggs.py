num_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for egg in range(num_eggs):
    colour = input()  # "red", "orange", "blue", "green"

    if colour == "red":
        red_eggs += 1
    elif colour == "orange":
        orange_eggs += 1
    elif colour == "blue":
        blue_eggs += 1
    else:
        green_eggs += 1

most_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)
colour_most_eggs = ""

if most_eggs == red_eggs:
    colour_most_eggs = "red"
elif most_eggs == orange_eggs:
    colour_most_eggs = "orange"
elif most_eggs == blue_eggs:
    colour_most_eggs = "blue"
else:
    colour_most_eggs = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {most_eggs} -> {colour_most_eggs}")
