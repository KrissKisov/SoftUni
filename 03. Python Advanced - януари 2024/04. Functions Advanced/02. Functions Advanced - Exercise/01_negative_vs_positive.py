def numbers(*integers):
    negative = []
    positive = []

    for num in integers:
        if num > 0:
            positive.append(num)

        elif num < 0:
            negative.append(num)

    negative_sum = sum(negative)
    positive_sum = sum(positive)

    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


# given_integers = [int(x) for x in input().split()]
# numbers(*given_integers)
numbers(*[int(x) for x in input().split()])
