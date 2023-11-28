encrypted_message = input()
command = input()
while command != "Decode":
    instructions = command.split("|")
    action = instructions[0]
    if action == "Move":
        number = int(instructions[1])
        encrypted_message = encrypted_message[number:] + encrypted_message[:number]

    elif action == "Insert":
        index, value = int(instructions[1]), instructions[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
