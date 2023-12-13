import re

text_string = input()
pattern = r"([|#])(?P<food>[A-Za-z\s]+)(\1)(?P<expiration_date>\d\d\/\d\d\/\d\d)(\1)(?P<calories>\d+)(\1)"
all_matches = list(re.finditer(pattern, text_string))
total_calories = 0
for match in all_matches:
    total_calories += int(match.group("calories"))
days_with_food = total_calories // 2000
print(f"You have food to last you for: {days_with_food} days!")
for match in all_matches:
    print(f"Item: {match.group('food')}, Best before: {match.group('expiration_date')}, Nutrition: {match.group('calories')}")
