expression = input()
stack = []

for current_index in range(len(expression)):
    if expression[current_index] == "(":
        stack.append(current_index)

    elif expression[current_index] == ")":
        if not stack:
            continue

        start = stack.pop()
        print(expression[start:current_index + 1])
