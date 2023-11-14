morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
              "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
              "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
              ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
              "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

words = input().split(" | ")
for word in words:
    current_word = word.split()
    decrypted_word = ""
    for letter in current_word:
        if letter in morse_code.keys():
            decrypted_word += morse_code[letter]
    print(decrypted_word, end=" ")
