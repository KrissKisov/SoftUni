subscription = int(input())

trainers = subscription - (subscription * 40/100)
training_kit = trainers - (trainers * 20/100)
ball = training_kit *  25/100
accessories = ball * 20/100

total_amount = subscription + trainers + training_kit + ball + accessories

print(total_amount)