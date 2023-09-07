deposit = float(input())
duration_of_deposit = int(input())
annual_interest_in_percent = float(input()) / 100

amount = deposit + duration_of_deposit * ((deposit * annual_interest_in_percent) / 12)

print(amount)