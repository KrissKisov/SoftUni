def hidden_message(given_string: str) -> str:
    numbers_list = [int(symbol) for symbol in given_string if symbol.isnumeric()]
    non_numbers_list = [symbol for symbol in given_string if not symbol.isnumeric()]

    take_list = [numbers_list[number] for number in range(len(numbers_list)) if number % 2 == 0]
    skip_list = [numbers_list[number] for number in range(len(numbers_list)) if number % 2 != 0]
    result_string = ""
    start_index = 0
    for i in range(len(take_list)):
        to_take = take_list[i]
        if start_index + to_take > 0:
            taken_string = "".join(non_numbers_list[start_index:start_index+to_take])
            result_string += taken_string
        to_skip = skip_list[i]
        start_index += to_skip + to_take
    return result_string


initial_string = input()

print(hidden_message(initial_string))
