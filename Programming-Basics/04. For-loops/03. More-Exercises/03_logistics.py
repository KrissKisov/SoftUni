freight = int(input())
van_price = 200  # ... <= 3 tonnes
truck_price = 175  # 4 <= ... <= 11 tonnes
train_price = 120  # ... >= 12 tonnes
total_van_load = 0
total_truck_load = 0
total_train_load = 0
total_price = 0
for _ in range(freight):
    load_weight = int(input())
    if load_weight <= 3:
        total_van_load += load_weight
        total_price += van_price * load_weight
    elif load_weight <= 11:
        total_truck_load += load_weight
        total_price += truck_price * load_weight
    elif load_weight >= 12:
        total_train_load += load_weight
        total_price += train_price * load_weight

total_weight = total_van_load + total_truck_load + total_train_load
average_price = total_price / total_weight
van_load_percent = total_van_load / total_weight * 100
truck_load_percent = total_truck_load / total_weight * 100
train_load_percent = total_train_load / total_weight * 100

print(f"{average_price :.2f}")
print(f"{van_load_percent :.2f}%")
print(f"{truck_load_percent :.2f}%")
print(f"{train_load_percent :.2f}%")
