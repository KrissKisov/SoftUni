chrysanthemum_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()  # [Spring, Summer, Аutumn, Winter]
day = input()  # [Y – да / N - не]

total_flowers = chrysanthemum_count + roses_count + tulip_count
arranging = 2
chrysanthemum_price = 0
roses_price = 0
tulip_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.1
    tulip_price = 2.5
    if day == "Y":
        chrysanthemum_price *= 1.15
        roses_price *= 1.15
        tulip_price *= 1.15
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulip_price = 4.15
    if day == "Y":
        chrysanthemum_price *= 1.15
        roses_price *= 1.15
        tulip_price *= 1.15

bouquet_price = (chrysanthemum_count * chrysanthemum_price) \
                + (roses_count * roses_price)  \
                + (tulip_count * tulip_price)
if tulip_count > 7 and season == "Spring":
    bouquet_price *= 0.95
elif roses_count >= 10 and season == "Winter":
    bouquet_price *= 0.9

if total_flowers > 20:
    bouquet_price *= 0.8

total_price = arranging + bouquet_price
print(f"{total_price :.2f}")
