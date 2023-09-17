months = int(input())

water = 20
internet = 15
others = 0
total_electricity = 0
total_others = 0
for month in range(months):
    electricity = float(input())
    others += (electricity + water + internet) +((electricity + water + internet) * 0.2)
    total_electricity += electricity

total_water = water * months
total_internet = internet * months
total_others += others
average = (total_electricity + total_water + total_internet + total_others) / months
print(f"Electricity: {total_electricity :.2f} lv")
print(f"Water: {total_water :.2f} lv")
print(f"Internet: {total_internet :.2f} lv")
print(f"Other: {total_others :.2f} lv")
print(f"Average: {average :.2f} lv")
