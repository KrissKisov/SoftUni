# def string_of_characters(first: str, last: str) -> str:
#     string = " ".join([chr(character) for character in range(ord(first) + 1, ord(last))])
#
#     return string
#
#
# first_character = input()
# last_character = input()
# print(string_of_characters(first_character, last_character))


def string_of_characters(first: str, last: str) -> str:
    string_as_list = []
    for character in range(ord(first) + 1, ord(last)):
        string_as_list.append(chr(character))
    return " ".join(string_as_list)


first_character = input()
last_character = input()
print(string_of_characters(first_character, last_character))
