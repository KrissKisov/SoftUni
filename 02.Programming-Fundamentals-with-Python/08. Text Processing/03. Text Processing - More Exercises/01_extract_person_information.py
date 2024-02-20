number = int(input())

for iteration in range(number):
    some_strings = input()
    name = ""
    age = ""
    if "@" in some_strings and "|" in some_strings:
        start_index_name = some_strings.index("@") + 1
        end_index_name = some_strings.index("|")
        name = some_strings[start_index_name:end_index_name]
    if "#" in some_strings and "*" in some_strings:
        start_index_age = some_strings.index("#") + 1
        end_index_age = some_strings.index("*")
        age = some_strings[start_index_age:end_index_age]

    print(f"{name} is {age} years old.")
