def age_assignment(*names, **letter_age):
    # 1
    person_info = []

    for name in names:
        for letter in letter_age:
            if name.startswith(letter):
                person_info.append([name, letter_age[letter]])

    person_info.sort()

    return '\n'.join(f"{person[0]} is {person[1]} years old." for person in person_info)

    ## 2
    # person_info = [[name, letter_age[letter]] for letter in letter_age for name in names if name.startswith(letter)]
    # person_info.sort()
    #
    # return '\n'.join(f"{person[0]} is {person[1]} years old." for person in person_info)

    ## 3
    # person_info = sorted([name, letter_age[letter]] for letter in letter_age for name in names if name.startswith(letter))
    #
    # return '\n'.join(f"{person[0]} is {person[1]} years old." for person in person_info)


# print(age_assignment("Peter", "George", G=26, P=19))
# print()
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
