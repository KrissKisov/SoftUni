from collections import deque


vowels_queue = deque(input().split())
consonants_list = input().split()
flowers = ["rose", "tulip", "lotus", "daffodil"]
searched_words = {"rose": "", "tulip": "", "lotus": "", "daffodil": ""}
found_word = None

while vowels_queue and consonants_list:

    vowel = vowels_queue.popleft()
    consonant = consonants_list.pop()

    for flower in flowers:

        if vowel in flower and vowel not in searched_words[flower]:
            searched_words[flower] += (flower.count(vowel) * vowel)

        if consonant in flower and consonant not in searched_words[flower]:
            searched_words[flower] += (flower.count(consonant) * consonant)

        if len(flower) == len(searched_words[flower]):
            found_word = flower
            break

    if found_word:
        break

if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels_queue:
    print(f"Vowels left: {' '.join(vowels_queue)}")

if consonants_list:
    print(f"Consonants left: {' '.join(consonants_list)}")
