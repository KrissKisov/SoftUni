pages_in_book = int(input())
read_pages_per_hour = int(input())
days_per_book = int(input())

hours_per_book = int(pages_in_book / read_pages_per_hour)
hours_per_day = int(hours_per_book / days_per_book)

print(hours_per_day)