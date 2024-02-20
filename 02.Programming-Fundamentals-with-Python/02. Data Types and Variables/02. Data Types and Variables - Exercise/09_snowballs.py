number_of_snowballs = int(input())
best_snowball_value = 0
best_snowball_quality = 0
best_snowball_weight = 0
best_snowball_time = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if best_snowball_value < current_snowball_value:
        best_snowball_value = current_snowball_value
        best_snowball_quality = snowball_quality
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})")
