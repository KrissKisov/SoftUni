def data_manipulation(first: str, second: str):
    if first == "int":
        return f"{int(second) * 2 :.0f}"
    elif first == "real":
        return f"{float(second) * 1.5 :.2f}"
    elif first == "string":
        return f"{1 * '$'}{second}{1 * '$'}"


first_line_input = input()
second_line_input = input()
print(data_manipulation(first_line_input, second_line_input))
