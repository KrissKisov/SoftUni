def even_odd(*args):
    command = args[-1]
    result_list = []

    if command == "even":
        result_list.extend([x for x in args[:-1] if x % 2 == 0])

    elif command == "odd":
        result_list.extend([x for x in args[:-1] if x % 2 != 0])

    return result_list


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
