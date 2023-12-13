yearly_fee = int(input())
trainers = yearly_fee * 0.6
outfit = trainers * 0.8
ball = outfit * 0.25
accessories = ball * 0.2

expenses = yearly_fee + trainers + outfit + ball + accessories

print(f"{expenses :.2f}")
