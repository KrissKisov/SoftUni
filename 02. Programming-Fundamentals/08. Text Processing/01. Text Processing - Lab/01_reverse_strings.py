given_string = input()

while not given_string.endswith("end"):
    # reversed_string = "".join([letter for letter in reversed(given_string)])
    reversed_string = given_string[::-1]

    print(f"{given_string} = {reversed_string}")

    given_string = input()
