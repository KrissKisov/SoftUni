def words_sorting(*args):
    words = {}

    for word in args:
        total_sum = 0

        for letter in word:
            total_sum += ord(letter)

        words[word] = total_sum

    if sum(words.values()) % 2 == 0:
        words = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        words = dict(sorted(words.items(), key=lambda x: -x[1]))
    return '\n'.join(f"{key} - {value}" for key, value in words.items())

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
