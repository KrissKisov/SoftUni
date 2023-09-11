change = float(input())
amount_of_change = int(change * 100)
coin_count = 0
coin_2lv = 200
coin_1lv = 100
coin_50st = 50
coin_20st = 20
coin_10st = 10
coin_5st = 5
coin_2st = 2
coin_1st = 1
while amount_of_change > 0:
    if amount_of_change >= coin_2lv:
        amount_of_change -= coin_2lv
    elif amount_of_change >= coin_1lv:
        amount_of_change -= coin_1lv
    elif amount_of_change >= coin_50st:
        amount_of_change -= coin_50st
    elif amount_of_change >= coin_20st:
        amount_of_change -= coin_20st
    elif amount_of_change >= coin_10st:
        amount_of_change -= coin_10st
    elif amount_of_change >= coin_5st:
        amount_of_change -= coin_5st
    elif amount_of_change >= coin_2st:
        amount_of_change -= coin_2st
    elif amount_of_change >= coin_1st:
        amount_of_change -= coin_1st
    coin_count += 1

print(coin_count)
