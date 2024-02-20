command = input()

total_sum = 0
while command != "NoMoreMoney":
    amount = float(command)
    if amount < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {amount:.2f}")
    total_sum += amount
    command = input()

print(f"Total: {total_sum :.2f}")
