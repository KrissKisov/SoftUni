import os


symbols = ("-", ",", ".", "!", "?")

ABS_PATH = os.path.join(os.path.dirname(__file__))
path = os.path.join(ABS_PATH, "new_folder", "text.txt")

with open(path) as file:
    text = file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:

        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1])
