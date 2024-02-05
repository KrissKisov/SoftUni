import os
import re


words_path = os.path.join("new_folder", "words.txt")
text_path = os.path.join("new_folder", "input.txt")
output_path = os.path.join("new_folder", "output_text.txt")

with open(words_path, "w") as file:
    file.write("quick is fault")

with open(text_path, "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here…It is safer.")

with open(words_path) as file:
    searched_words_text = file.read()
    searched_words_list = [word.lower() for word in searched_words_text.split()]

with open(text_path) as file:
    text = file.read().lower()

words_count = {}

for word in searched_words_list:
    pattern = re.compile(rf"\b{word}\b")
    result = re.findall(pattern, text)
    words_count[word] = len(result)

sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, "w") as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")
