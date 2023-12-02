# encrypted_message = input()
# command = input()
# while command != "Decode":
#     instructions = command.split("|")
#     action = instructions[0]
#     if action == "Move":
#         number = int(instructions[1])
#         encrypted_message = encrypted_message[number:] + encrypted_message[:number]
#
#     elif action == "Insert":
#         index, value = int(instructions[1]), instructions[2]
#         encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
#
#     elif action == "ChangeAll":
#         substring, replacement = instructions[1], instructions[2]
#         if substring in encrypted_message:
#             encrypted_message = encrypted_message.replace(substring, replacement)
#
#     command = input()
#
# print(f"The decrypted message is: {encrypted_message}")


def move(message, number):
    message = message[number:] + message[:number]
    return message


def insert(message, some_index, some_value):
    message = message[:some_index] + value + message[some_index:]
    return message


def change_all(message, old_text, new_text):
    message = message.replace(old_text, new_text)
    return message


encrypted_message = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break

    elif command[0] == "Move":
        num_of_letters = int(command[1])
        encrypted_message = move(encrypted_message, num_of_letters)

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = insert(encrypted_message, index, value)

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)
