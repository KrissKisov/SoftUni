key_number = int(input())
number_of_letters = int(input())
message = []
for letter in range(number_of_letters):
    current_letter = input()
    message.append(chr(ord(current_letter) + key_number))
decrypted_message = "".join(message)
print(decrypted_message)
