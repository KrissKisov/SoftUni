# favourite_book = input()
# book_count = 0
# current_book = input()
# while current_book != "No More Books":
#     if current_book == favourite_book:
#         print(f"You checked {book_count} books and found it.")
#         break
#     book_count += 1
#     current_book = input()
# else:
#     print("The book you search is not here!")
#     print(f"You checked {book_count} books.")

favourite_book = input()
book_count = 0
current_book = input()
while current_book != "No More Books":
    if current_book == favourite_book:
        break
    book_count += 1
    current_book = input()

if current_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")
