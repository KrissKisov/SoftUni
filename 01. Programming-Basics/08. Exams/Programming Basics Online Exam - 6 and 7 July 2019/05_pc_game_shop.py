sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for _ in range(sold_games):
    game = input()

    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

percent_hearthstone = hearthstone / sold_games * 100
percent_fornite = fornite / sold_games * 100
percent_overwatch = overwatch / sold_games * 100
percent_others = others / sold_games * 100

print(f"Hearthstone - {percent_hearthstone :.2f}%")
print(f"Fornite - {percent_fornite :.2f}%")
print(f"Overwatch - {percent_overwatch :.2f}%")
print(f"Others - {percent_others :.2f}%")
