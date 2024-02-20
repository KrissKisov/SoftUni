juniors_bikers = int(input())
seniors_bikers = int(input())
track = input()  # "trail", "cross-country", "downhill" или "road"

junior_fee = 0
senior_fee = 0
if track == "trail":
    junior_fee = 5.5
    senior_fee = 7
elif track == "cross-country":
    junior_fee = 8
    senior_fee =9.5
    if juniors_bikers + seniors_bikers >= 50:
        junior_fee *= 0.75
        senior_fee *= 0.75
elif track == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif track == "road":
    junior_fee = 20
    senior_fee = 21.5

total_fee = juniors_bikers * junior_fee + seniors_bikers * senior_fee
expenses = total_fee * 0.05
amount_for_charity = total_fee - expenses
print(f"{amount_for_charity :.2f}")
