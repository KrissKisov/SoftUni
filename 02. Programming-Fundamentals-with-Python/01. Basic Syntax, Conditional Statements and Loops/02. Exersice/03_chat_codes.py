number_of_messages = int(input())

for number in range(number_of_messages):
    message_code = int(input())

    if message_code == 88:
        print("Hello")
    elif message_code == 86:
        print("How are you?")
    elif message_code < 88:
        print("GREAT!")
    else:  # message_code > 88
        print("Bye.")
