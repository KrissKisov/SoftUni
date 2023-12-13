import re

word_pairs = []
text_string = input()
pattern = r"(?i)([@|#])(?P<first>[a-z]{3,})(\1)(\1)(?P<second>[a-z]{3,})(\1)"
results = re.finditer(pattern, text_string)
for res in results:
    word_pairs.append(res.group("first") + ':' + res.group("second"))

if len(word_pairs) > 0:
    print(f"{len(word_pairs)} word pairs found!")
    mirror_words = []
    for pair in word_pairs:
        first_word, second_word = pair.split(":")
        if first_word == second_word[::-1]:
            mirror_words.append(first_word + " <=> " + second_word)

    if len(mirror_words) > 0:
        print(f"The mirror words are:")
        print(f"{', '.join(mirror_words)}")
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")
