secret_message = input().split()
deciphered_message = []

for word in range(len(secret_message)):
    current_word = list(secret_message[word])
    digits_in_word = []
    for letter in range(len(current_word)):
        if current_word[letter].isdigit():
            digits_in_word.append(current_word[letter])
    first_letter = chr(int("".join([x for x in digits_in_word])))
    length_of_digits = len(digits_in_word)
    current_word[:length_of_digits] = first_letter
    current_word[1],current_word[-1] = current_word[-1], current_word[1]
    deciphered_word = "".join(current_word)
    deciphered_message.append(deciphered_word)

print(*deciphered_message)
