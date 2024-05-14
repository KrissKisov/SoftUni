odd_set = set()
even_set = set()

for number in range(1, int(input()) + 1):
    name = input()
    ascii_sum = sum(ord(x) for x in name) // number

    if ascii_sum % 2 != 0:
        odd_set.add(ascii_sum)

    else:
        even_set.add(ascii_sum)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    print(*(odd_set.union(even_set)), sep=', ')

elif sum_odd_set > sum_even_set:
    print(*(odd_set.difference(even_set)), sep=', ')

elif sum_odd_set < sum_even_set:
    print(*(odd_set.symmetric_difference(even_set)), sep=', ')
