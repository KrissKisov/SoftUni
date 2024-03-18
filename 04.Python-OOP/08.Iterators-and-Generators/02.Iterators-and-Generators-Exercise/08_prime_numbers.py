from math import sqrt
from typing import List


def get_primes(integers: List[int]):

    for number in integers:

        if number <= 1:
            continue

        for num in range(2, int(sqrt(number)) + 1):  # isqrt() == int(sqrt()) but not passing in judge
            if number % num == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
