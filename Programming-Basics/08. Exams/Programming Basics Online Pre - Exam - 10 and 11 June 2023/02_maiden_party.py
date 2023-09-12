maiden_party_price = float(input())
love_message_count = int(input())
wax_roses_count = int(input())
key_holder_count = int(input())
cartoon_count = int(input())
lucky_surprise_count = int(input())

total_count = love_message_count + wax_roses_count + key_holder_count + cartoon_count \
              + lucky_surprise_count
love_message_price = 0.60
wax_rose_price = 7.20
key_holder_price = 3.60
cartoon_price = 18.20
lucky_surprise_price = 22
discount = 0.35
hosting_fee = 0.1
earned_money = (love_message_count * love_message_price) + (wax_roses_count * wax_rose_price) \
               + (key_holder_count * key_holder_price) + (cartoon_count * cartoon_price) \
               + (lucky_surprise_count * lucky_surprise_price)
if total_count >= 25:
    earned_money *= 0.65

total_earned_money = earned_money * 0.9
difference = total_earned_money - maiden_party_price
if total_earned_money >= maiden_party_price:
    print(f"Yes! {difference :.2f} lv left.")
else:
    print(f"Not enough money! {abs(difference) :.2f} lv needed.")
