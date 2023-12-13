concealed_message = input()

while True:
    command = input().split(":|:")
    if "Reveal" in command:
        print(f"You have a new text message: {concealed_message}")
        break

    elif "InsertSpace" in command:
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif "Reverse" in command:
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print("error")

    elif "ChangeAll" in command:
        substring_to_change = command[1]
        replacement = command[2]
        concealed_message = concealed_message.replace(substring_to_change, replacement)
        print(concealed_message)
