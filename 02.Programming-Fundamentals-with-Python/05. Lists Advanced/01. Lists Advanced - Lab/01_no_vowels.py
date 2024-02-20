# given_text = input()
# given_text_as_list = list(given_text)
# vowels = ['a', 'o', 'u', 'e', 'i']
# for letter in given_text:
#     if letter.lower() in vowels:
#         given_text_as_list.remove(letter)
# print("".join(given_text_as_list))

given_text = input()
vowels_to_exclude = ['a', 'o', 'u', 'e', 'i']
output_text = [letter for letter in given_text if letter.lower() not in vowels_to_exclude]
print("".join(output_text))
