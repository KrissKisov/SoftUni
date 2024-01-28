def func_executor(*tuples):

    # return "\n".join(f"{func_to_call.__name__} - {func_to_call(*arguments)}" for func_to_call, arguments in tuples)
    #
    result = ""

    for func_to_call, arguments in tuples:
        result += f"{func_to_call.__name__} - {func_to_call(*arguments)}\n"

    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
