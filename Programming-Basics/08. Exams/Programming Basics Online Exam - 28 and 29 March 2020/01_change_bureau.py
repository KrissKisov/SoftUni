bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input())

bitcoin_to_lev = 1168
yuan_to_dollar = 0.15
dollar_to_lev = 1.76
euro_to_lev = 1.95

euro_can_buy = (bitcoins * bitcoin_to_lev + (chinese_yuan * yuan_to_dollar) * dollar_to_lev) / euro_to_lev
available_euro = euro_can_buy - euro_can_buy * commission / 100

print(f"{available_euro :.2f}")
