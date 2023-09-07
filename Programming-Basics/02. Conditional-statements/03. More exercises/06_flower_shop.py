import math

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

total_sum = magnolias * magnolia_price \
            + hyacinth_price * hyacinths \
            + rose_price * roses \
            + cactus_price * cacti
total_sum -= total_sum * 0.05

if total_sum >= gift_price:
    print(f"She is left with {math.floor(total_sum - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_sum)} leva.")
