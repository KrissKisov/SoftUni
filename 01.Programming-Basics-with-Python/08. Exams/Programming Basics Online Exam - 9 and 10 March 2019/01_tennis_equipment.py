from math import floor, ceil


tennis_racket_price = float(input())
number_rackets = int(input())
pair_trainers_num = int(input())
trainers_price = tennis_racket_price / 6
other_equipment = (number_rackets * tennis_racket_price + pair_trainers_num * trainers_price) * 0.2
total_price = number_rackets * tennis_racket_price + pair_trainers_num * trainers_price + other_equipment

player_amount = floor(total_price / 8)
sponsor_amount = ceil(total_price * 7 / 8)

print(f"Price to be paid by Djokovic {player_amount}")
print(f"Price to be paid by sponsors {sponsor_amount}")
