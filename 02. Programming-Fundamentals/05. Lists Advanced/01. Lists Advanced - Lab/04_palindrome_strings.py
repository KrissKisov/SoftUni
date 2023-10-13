# def palindrome(words: list) -> list:
#     palindromes_list = []
#     for word in words:
#         if word == word[::-1]:
#             palindromes_list.append(word)
#
#     return palindromes_list
#
#
# def palindromes_count(word: str) -> int:
#     found_palindromes = list_of_palindromes.count(word)
#     return found_palindromes
#
#
# list_of_words = input().split()
# palindrome_word = input()
# list_of_palindromes = palindrome(list_of_words)
# number_of_appearing = palindromes_count(palindrome_word)
# print(list_of_palindromes)
# print(f"Found palindrome {number_of_appearing} times")

def palindrome(words: list) -> list:
    return [word for word in words if word == word[::-1]]


list_of_words = input().split()
palindrome_word = input()
list_of_palindromes = palindrome(list_of_words)
number_of_appearing = list_of_palindromes.count(palindrome_word)
print(list_of_palindromes)
print(f"Found palindrome {number_of_appearing} times")
