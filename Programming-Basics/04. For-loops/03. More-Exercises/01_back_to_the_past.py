inherited_money = float(input())
year_to_live = int(input())  # included

money_to_spent = 0
age = 18
for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        money_to_spent += 12000
    else:
        money_to_spent += 12000 + 50 * age
    age += 1

left_or_needed_money = abs(inherited_money - money_to_spent)
if inherited_money >= money_to_spent:
    print(f"Yes! "
          f"He will live a carefree life and will have {left_or_needed_money :.2f} dollars left.")
else:
    print(f"He will need {left_or_needed_money :.2f} dollars to survive.")
