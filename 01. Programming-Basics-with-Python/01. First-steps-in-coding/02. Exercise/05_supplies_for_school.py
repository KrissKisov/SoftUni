PACK_OF_PENS = 5.80
PACK_OF_MARKERS = 7.20
DETERGENT_IN_LITRE = 1.20

pens = int(input()) * PACK_OF_PENS
markers = int(input()) * PACK_OF_MARKERS
litres_of_detergent = int(input()) * DETERGENT_IN_LITRE
discount = int(input()) / 100

total_price = pens + markers + litres_of_detergent
final_price = total_price - (total_price * discount)

print(final_price)