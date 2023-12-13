cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    split_deck = len(cards) // 2
    left_part = cards[:split_deck]
    right_part = cards[split_deck:]
    shuffle_deck = []
    for card in range(split_deck):
        shuffle_deck.append(left_part[card])
        shuffle_deck.append(right_part[card])

    cards = shuffle_deck

print(cards)
