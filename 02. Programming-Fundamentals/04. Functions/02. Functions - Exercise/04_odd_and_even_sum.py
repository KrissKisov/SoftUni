def sum_of_odd_and_even(string: str) -> str:
    sum_of_odd = 0
    sum_of_even = 0
    for symbol in number_as_string:
        number = int(symbol)
        if number % 2 != 0:
            sum_of_odd += number
        else:
            sum_of_even += number

    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number_as_string = input()
print(sum_of_odd_and_even(number_as_string))
