given_string = input()
digits = ""
letters = ""
symbols = ""

for i in given_string:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:  # elif not i.isalnum():
        symbols += i

print(digits)
print(letters)
print(symbols)
