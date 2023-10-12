def factorial(first: int, second: int) -> float:
    first_number = 1
    for i in range(1, first + 1):
        first_number *= i

    second_number = 1
    for j in range(1, second + 1):
        second_number *= j

    return first_number / second_number


first_integer = int(input())
second_integer = int(input())
result = factorial(first_integer, second_integer)
print(f"{result :.2f}")
