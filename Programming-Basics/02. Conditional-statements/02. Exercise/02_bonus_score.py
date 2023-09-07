score = int(input())
bonus_score = 0
# extra_bonus_score = 0

if score <= 100:
    bonus_score = 5
elif score <= 1000:
    bonus_score = score * 0.20
else:
    bonus_score = score * 0.10

# if score % 2 == 0:
#     extra_bonus_score = 1
# elif score % 10 == 5:
#     extra_bonus_score = 2
#
# print(bonus_score + extra_bonus_score)
# print(score + bonus_score + extra_bonus_score)

if score % 2 == 0:
    bonus_score += 1
elif score % 10 == 5:
    bonus_score += 2

print(bonus_score)
print(score + bonus_score)
