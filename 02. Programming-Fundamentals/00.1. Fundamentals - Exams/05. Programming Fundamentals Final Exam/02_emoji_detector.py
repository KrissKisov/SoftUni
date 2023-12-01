import re


some_text = input()
emoji_pattern = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)"
threshold_pattern = r"\d"
valid_emojis = {}
cool_threshold = 1
emojis = re.findall(emoji_pattern, some_text)
threshold = re.findall(threshold_pattern, some_text)
for emoji in emojis:
    emoji_coolness = 0
    for letter in emoji[1]:
        emoji_coolness += ord(letter)
    valid_emojis["".join(emoji)] = emoji_coolness
for char in threshold:
    cool_threshold *= int(char)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for key, value in valid_emojis.items():
    if valid_emojis[key] > cool_threshold:
        print(key)