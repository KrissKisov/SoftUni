import re

sentence = input()
searched_word = input()
# pattern = fr"\b{searched_word}\b"
pattern = fr"(?i)\b{searched_word}\b"
# result = re.findall(pattern, sentence, re.IGNORECASE)
result = re.findall(pattern, sentence)
print(len(result))
