number_of_integers = int(input())
positive_list = []
negative_list = []
for _ in range(number_of_integers):
    integer = int(input())

    if integer >= 0:
        positive_list.append(integer)
    else:
        negative_list.append(integer)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
