sequence = input().split()
occurrence = {}

for word in sequence:
    if word.lower() not in occurrence:
        occurrence[word.lower()] = 0
    occurrence[word.lower()] += 1

print(" ".join(key for key, value in occurrence.items() if value % 2 != 0))
