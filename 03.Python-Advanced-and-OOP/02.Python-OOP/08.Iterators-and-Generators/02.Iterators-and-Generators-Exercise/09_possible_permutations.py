from itertools import permutations


def possible_permutations(iterable: list):
    for x in permutations(iterable):
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]