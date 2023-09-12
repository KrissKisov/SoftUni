initial_quantity = int(input())
command = input()  # "Close", "Buy" или "Fill"
sold_eggs = 0

while command != "Close":
    buy_or_fill = command
    num_eggs = int(input())

    if buy_or_fill == "Buy":
        if num_eggs > initial_quantity:
            break
        else:
            initial_quantity -= num_eggs
            sold_eggs += num_eggs
    else:
        initial_quantity += num_eggs

    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {initial_quantity}.")
