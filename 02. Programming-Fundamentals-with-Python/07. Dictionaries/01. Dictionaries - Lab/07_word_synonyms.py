number_of_words = int(input())
synonyms = {}

for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms.keys():
    print(f"{key} - {', '.join(synonyms[key])}")
