from math import floor


cat_breed = input()  # "British Shorthair", "Siamese", "Persian", "Ragdoll",
# "American Shorthair" или "Siberian"
gender = input()  # 'm' или 'f'

average_life = 0
if cat_breed == "British Shorthair":
    if gender == "m":
        average_life = 13 * 12 / 6
    else:
        average_life = 14 * 12 / 6
    print(f"{floor(average_life)} cat months")
elif cat_breed == "Siamese":
    if gender == "m":
        average_life = 15 * 12 / 6
    else:
        average_life = 16 * 12 / 6
    print(f"{floor(average_life)} cat months")
elif cat_breed == "Persian":
    if gender == "m":
        average_life = 14 * 12 / 6
    else:
        average_life = 15 * 12 / 6
    print(f"{floor(average_life)} cat months")
elif cat_breed == "Ragdoll":
    if gender == "m":
        average_life = 16 * 12 / 6
    else:
        average_life = 17 * 12 / 6
    print(f"{floor(average_life)} cat months")
elif cat_breed == "American Shorthair":
    if gender == "m":
        average_life = 12 * 12 / 6
    else:
        average_life = 13 * 12 / 6
    print(f"{floor(average_life)} cat months")
elif cat_breed == "Siberian":
    if gender == "m":
        average_life = 11 * 12 / 6
    else:
        average_life = 12 * 12 / 6
    print(f"{floor(average_life)} cat months")
else:
    print(f"{cat_breed} is invalid cat!")
