money_for_beggars = input().split(", ")
number_of_beggars = int(input())
money_taken = []
for beggar in range(number_of_beggars):
    current_money = 0
    for money in range(beggar, len(money_for_beggars), number_of_beggars):
        current_money += int(money_for_beggars[money])

    money_taken.append(current_money)

print(money_taken)
