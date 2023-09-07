mackerel_price = float(input()) #skumria
sprat_price = float(input()) #tzatza
bonito_in_kg = float(input()) #palamud
safrid_in_kg = float(input())
mussels_in_kg = int(input()) #midi
bonito_price = mackerel_price + mackerel_price * 0.6
safrid_price = sprat_price + sprat_price * 0.8
mussels_price = 7.50

amount = bonito_in_kg * bonito_price \
         + safrid_in_kg * safrid_price \
         + mussels_in_kg * mussels_price

print(f"{amount:.2f}")