def accommodate_new_pets(capacity, max_weight, *pets_info):

    all_pets_accommodated = True
    pets = {}

    for pet_info in pets_info:

        if capacity <= 0:
            all_pets_accommodated = False
            break

        pet_type, pet_weight = pet_info

        if float(pet_weight) <= max_weight:

            if pet_type not in pets.keys():
                pets[pet_type] = 0

            pets[pet_type] += 1
            capacity -= 1

    pets = sorted(pets.items(), key=lambda x: x[0])
    result = ""

    if capacity == 0 and all_pets_accommodated:
        result += f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n" + '\n'.join(str(f"{k}: {v}") for k, v in pets)
        return result
    elif capacity > 0:
        result += f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n" + '\n'.join(
            str(f"{k}: {v}") for k, v in pets)
        return result
    else:
        result += f"You did not manage to accommodate all pets!\nAccommodated pets:\n" + '\n'.join(str(f"{k}: {v}") for k, v in pets)
        return result


print(accommodate_new_pets(
    5,
    5.0,
    ("fish", 5.2),
    ("fish", 6.3),
    ("fish", 0.1),
    ("fish", 0.2),
    ("fish", 0.5),
    ("fish", 0.4),
    ("fish", 0.3))
)
print(accommodate_new_pets(
    2,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

# # outputs
# All pets are accommodated! Available capacity: 8.
# Accommodated pets:
# cat: 1
# dog: 1
#
# All pets are accommodated! Available capacity: 7.
# Accommodated pets:
# cat: 2
# parrot: 1
#
# You did not manage to accommodate all pets!
# Accommodated pets:
# cat: 1
# dog: 1
