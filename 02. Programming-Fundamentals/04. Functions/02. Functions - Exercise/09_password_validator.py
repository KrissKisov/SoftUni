# def length_validation(some_password: str) -> bool:
#     if 6 <= len(some_password) <= 10:
#         return True
#     print("Password must be between 6 and 10 characters")
#     return False
#
#
# def letter_digit_only_validation(some_password: str) -> bool:
#     if some_password.isalnum():
#         return True
#     print("Password must consist only of letters and digits")
#     return False
#
#
# def enough_digits_validation(some_password: str) -> bool:
#     digits_in_password = []
#     for symbol in some_password:
#         if symbol.isdigit():
#             digits_in_password.append(symbol)
#     if len(digits_in_password) >= 2:
#         return True
#     print("Password must have at least 2 digits")
#     return False
#
#
# def password_validation(some_password: str) -> bool:
#     length_is_valid = length_validation(some_password)
#     valid_symbols = letter_digit_only_validation(some_password)
#     enough_digits = enough_digits_validation(some_password)
#
#     if length_is_valid and enough_digits and valid_symbols:
#         return True
#
#
# password = input()
# password_is_valid = password_validation(password)
# if password_is_valid:
#     print("Password is valid")


def valid_pass(some_pass: str):
    is_valid = True
    if len(some_pass) not in range(6, 10 + 1):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not some_pass.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    digit_count = 0
    for symbol in some_pass:
        if symbol.isdigit():
            digit_count += 1
    if digit_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
valid_pass(password)
