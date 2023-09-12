word = input()
the_most_powerful_word = ""
word_power = 0

while word != "End of words":
    current_word_power = 0

    for letter in word:
        current_word_power += ord(letter)

    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        current_word_power *= len(word)
    else:
        current_word_power = int(current_word_power / len(word))

    if word_power < current_word_power:
        word_power = current_word_power
        the_most_powerful_word = word

    word = input()

print(f"The most powerful word is {the_most_powerful_word} - {word_power}")
