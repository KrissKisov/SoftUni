eggs_size = input()  # "Large", "Medium" или "Small"
colour = input()  # "Red", "Green" или "Yellow"
num_batches = int(input())
batch_price = 0

if eggs_size == "Large":
    if colour == "Red":
        batch_price = 16
    elif colour == "Green":
        batch_price = 12
    else:
        batch_price = 9
elif eggs_size == "Medium":
    if colour == "Red":
        batch_price = 13
    elif colour == "Green":
        batch_price = 9
    else:
        batch_price = 7
else:
    if colour == "Red":
        batch_price = 9
    elif colour == "Green":
        batch_price = 8
    else:
        batch_price = 5

income = num_batches * batch_price
profit = income * 0.65
print(f"{profit :.2f} leva.")
