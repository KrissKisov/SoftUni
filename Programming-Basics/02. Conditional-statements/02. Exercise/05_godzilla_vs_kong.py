movie_budget = float(input())
actors = int(input())
outfit_price_per_actor = float(input())

decor = movie_budget * 0.10
discount_outfit = 0.10
total_outfit_amount = actors * outfit_price_per_actor

if actors > 150:
    total_outfit_amount = total_outfit_amount - total_outfit_amount * discount_outfit

money_needed = decor + total_outfit_amount

if money_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - money_needed:.2f} leva left.")
