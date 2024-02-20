age = float(input())
gender = input()

pronoun = ""
if age >=16:
    if gender == "m":
        pronoun = "Mr."
    elif gender == "f":
        pronoun = "Ms."
else:
    if gender == "m":
        pronoun = "Master"
    elif gender == "f":
        pronoun = "Miss"

print(pronoun)
