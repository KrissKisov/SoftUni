def treasure_coordinates(some_message: str) -> str:
    start_symbol = "<"
    end_symbol = ">"
    start_symbol_index = some_message.index(start_symbol)
    end_symbol_index = some_message.index(end_symbol)
    coordinates = some_message[start_symbol_index + 1:end_symbol_index]
    return coordinates


def treasure_type(some_message: str) -> str:
    symbol = "&"
    type_of_treasure = some_message.split(symbol)[1]
    return type_of_treasure


def message_decrypting(some_string: str, some_key: list) -> str:
    key_extension = "".join(some_key.copy())
    decrypted_message = ""
    if len(some_key) < len(some_string):
        key_extension *= len(some_string) // len(some_key)
        key_extension += "".join(some_key[:len(some_string) % len(some_key)])
    for index, char in enumerate(some_string):
        decrypted_message += chr(ord(char) - int(key_extension[index]))
    return decrypted_message


key = input().split()
command = input()

while command != "find":
    current_string = command
    current_message = message_decrypting(current_string, key)
    current_treasure = treasure_type(current_message)
    current_coordinates = treasure_coordinates(current_message)
    print(f"Found {current_treasure} at {current_coordinates}")

    command = input()
