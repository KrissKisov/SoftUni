from collections import deque


money_list = [int(x) for x in input().split()]
prices_queue = deque([int(x) for x in input().split()])

eaten_food_count = 0

while money_list and prices_queue:

    current_money = money_list.pop()
    current_price = prices_queue.popleft()

    if current_money == current_price:
        eaten_food_count += 1

    elif current_money > current_price:
        eaten_food_count += 1

        change = current_money - current_price

        if money_list:
            money_list[-1] += change
        else:
            money_list.append(change)

if eaten_food_count >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food_count} foods.")
elif eaten_food_count > 1:
    print(f"Henry ate: {eaten_food_count} foods.")
elif eaten_food_count == 1:
    print(f"Henry ate: {eaten_food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
