age = int(input())
washing_machine_price = float(input())
each_toy_price = int(input())

saved_money = 0
toys_count = 0
received_money = 0
for year in range(1, age + 1):
    if year % 2 == 0:
        received_money += 10
        saved_money += received_money - 1
    else:
        toys_count += 1

total_money = saved_money + toys_count * each_toy_price
if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price :.2f}")
else:
    print(f"No! {washing_machine_price - total_money :.2f}")
