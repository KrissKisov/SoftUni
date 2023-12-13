# def palindromes(numbers_list: list):
#     for number in numbers_list:
#         is_palindrome = True
#         if number == number[::-1]:
#             print(is_palindrome)
#         else:
#             is_palindrome = False
#             print(is_palindrome)
#
#
# list_of_integers = list(input().split(", "))
# palindromes(list_of_integers)

def is_palindrome(numbers: str) -> bool:
    return numbers == numbers[::-1]


list_of_integers = input().split(", ")
for number in list_of_integers:
    print(is_palindrome(number))
