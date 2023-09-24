number = int(input())

for first_letter in range(number):
    for second_letter in range(number):
        for third_letter in range(number):
            print(f"{chr(ord('a') + first_letter)}{chr(ord('a') + second_letter)}{chr(ord('a') + third_letter)}")
