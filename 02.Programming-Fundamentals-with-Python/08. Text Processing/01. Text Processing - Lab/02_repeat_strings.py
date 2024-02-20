words = input().split()
new_words = ""
for word in words:
    new_words += word * len(word)

print(new_words)
