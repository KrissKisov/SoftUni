PUZZLE = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

excursion_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bear_count = int(input())
minions_count = int(input())
trucks_count = int(input())
total_toys_count = puzzles_count + talking_dolls_count + teddy_bear_count + minions_count + trucks_count

total_earnings = puzzles_count * PUZZLE\
                 + talking_dolls_count * TALKING_DOLL\
                 + teddy_bear_count * TEDDY_BEAR \
                 + minions_count * MINION\
                 + trucks_count * TRUCK

discount = total_earnings * 0.25

if total_toys_count >= 50:
    total_earnings -= discount

rent = total_earnings * 0.10
money_left_after_rent = total_earnings - rent

if money_left_after_rent >= excursion_price:
    print(f"Yes! {money_left_after_rent - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - money_left_after_rent:.2f} lv needed.")
