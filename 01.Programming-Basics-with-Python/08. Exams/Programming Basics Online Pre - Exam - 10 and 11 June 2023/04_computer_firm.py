computers_count = int(input())
done_sells = 0
average_rating = 0
for _ in range(computers_count):
    current_number = int(input())
    current_rating = current_number % 10
    average_rating += current_rating
    possible_sells = current_number // 10
    if current_rating == 3:
        done_sells += possible_sells * 0.5
    elif current_rating == 4:
        done_sells += possible_sells * 0.7
    elif current_rating == 5:
        done_sells += possible_sells * 0.85
    elif current_rating == 6:
        done_sells += possible_sells

average_rating_all_computers = average_rating / computers_count
print(f"{done_sells :.2f}")
print(f"{average_rating_all_computers :.2f}")
