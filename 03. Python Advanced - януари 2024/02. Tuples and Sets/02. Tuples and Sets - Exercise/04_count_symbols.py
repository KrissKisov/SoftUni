text = input()
text_as_set = set(text)

for symbol in sorted(text_as_set):
    print(f"{symbol}: {text.count(symbol)} time/s")
