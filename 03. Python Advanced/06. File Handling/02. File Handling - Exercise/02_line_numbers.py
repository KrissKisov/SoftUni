import os

from string import punctuation


ABS_PATH = os.path.join(os.path.dirname(__file__))
path = os.path.join(ABS_PATH, "new_folder", "text.txt")
output_file = os.path.join(ABS_PATH, "new_folder", "output.txt")

with open(path) as file:
    text = file.readlines()

with open(output_file, "w") as file:

    for line in range(len(text)):

        letters = len([x for x in text[line] if x.isalpha()])
        marks = len([x for x in text[line] if x in punctuation])

        file.write(f"Line {line + 1}: {text[line][:-1]} ({letters})({marks})\n")
