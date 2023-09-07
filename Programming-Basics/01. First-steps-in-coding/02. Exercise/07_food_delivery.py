CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETERIAN_MENU = 8.15
DELIVERY = 2.50

count_chicken_menus = int(input()) * 10.35
count_fish_menus = int(input()) * 12.40
count_veggie_menus = int(input()) * 8.15
dessert = (count_chicken_menus + count_fish_menus + count_veggie_menus) * 20/100

order_price = count_chicken_menus + count_fish_menus + count_veggie_menus + dessert + DELIVERY

print(order_price)