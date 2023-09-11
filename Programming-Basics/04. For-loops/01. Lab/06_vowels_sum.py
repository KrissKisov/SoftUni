my_text = input()

vowels_sum = 0
for vowel in my_text:
    if vowel == "a":
        vowels_sum += 1
    elif vowel == "e":
        vowels_sum += 2
    elif vowel == "i":
        vowels_sum += 3
    elif vowel == "o":
        vowels_sum += 4
    elif vowel == "u":
        vowels_sum += 5
print(vowels_sum)
