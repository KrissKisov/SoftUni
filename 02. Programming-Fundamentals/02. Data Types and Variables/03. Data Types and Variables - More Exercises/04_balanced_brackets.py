number_of_lines = int(input())
opening_brackets_count = 0
closing_brackets_count = 0
for line in range(number_of_lines):
    line_input = input()
    if line_input == "(":
        if closing_brackets_count > opening_brackets_count:
            break

        opening_brackets_count += 1

        if opening_brackets_count - closing_brackets_count > 1:
            break

    elif line_input == ")":
        closing_brackets_count += 1

if opening_brackets_count == closing_brackets_count:
    print("BALANCED")
else:
    print("UNBALANCED")
