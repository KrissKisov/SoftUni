given_string = input()
string_lowercase = given_string.lower()
counter = 0

if "sand" in given_string.lower():
    sand = string_lowercase.count("sand")
    counter += sand
if "water" in given_string.lower():
    water = string_lowercase.count("water")
    counter += water
if "fish" in given_string.lower():
    fish = string_lowercase.count("fish")
    counter += fish
if "sun" in given_string.lower():
    sun = string_lowercase.count("sun")
    counter += sun

print(counter)
