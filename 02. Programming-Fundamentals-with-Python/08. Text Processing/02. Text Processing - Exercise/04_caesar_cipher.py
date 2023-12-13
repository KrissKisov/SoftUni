message = input()
new_message = ""
for char in message:
    new_char = chr(ord(char) + 3)
    new_message += new_char

print(new_message)
