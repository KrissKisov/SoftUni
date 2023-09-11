move_count = int(input())

points = 0
result = 0
between_0_9 = 0
between_10_19 = 0
between_20_29 = 0
between_30_39 = 0
between_40_50 = 0
invalid_numbers = 0
for move in range(move_count):
    number = int(input())
    if number < 0 or number > 50:
        result /= 2
        invalid_numbers += 1
    elif 0 <= number <= 9:
        points = number * 0.2
        between_0_9 += 1
        result += points
    elif number <= 19:
        points = number * 0.3
        between_10_19 += 1
        result += points
    elif number <= 29:
        points = number * 0.4
        between_20_29 += 1
        result += points
    elif number <= 39:
        points = 50
        between_30_39 += 1
        result += points
    elif number <= 50:
        points = 100
        between_40_50 += 1
        result += points

between_0_9_percent = between_0_9 / move_count * 100
between_10_19_percent = between_10_19 / move_count * 100
between_20_29_percent = between_20_29 / move_count * 100
between_30_39_percent = between_30_39 / move_count * 100
between_40_50_percent = between_40_50 / move_count * 100
invalid_numbers_percent = invalid_numbers / move_count * 100
print(f"{result :.2f}")
print(f"From 0 to 9: {between_0_9_percent :.2f}%")
print(f"From 10 to 19: {between_10_19_percent :.2f}%")
print(f"From 20 to 29: {between_20_29_percent :.2f}%")
print(f"From 30 to 39: {between_30_39_percent :.2f}%")
print(f"From 40 to 50: {between_40_50_percent :.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent :.2f}%")
