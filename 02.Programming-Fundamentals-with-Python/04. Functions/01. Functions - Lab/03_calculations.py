def calculate(action: str, first: int, second: int) -> int:
    result = 0
    if action == "multiply":
        result = first * second
    elif action == "divide":
        result = int(first / second)
    elif action == "add":
        result = first + second
    elif action == "subtract":
        result = first - second

    return result

operator = input()
first_number = int(input())
second_number = int(input())
print(calculate(operator, first_number, second_number))
