starting_letter = input()
finishing_letter = input()
skipping_letter = input()
starting_letter_as_num = ord(starting_letter)
finishing_letter_as_num = ord(finishing_letter)
skipping_letter_as_num = ord(skipping_letter)

combination = 0
for first_letter in range(starting_letter_as_num, finishing_letter_as_num + 1):
    for skipping in range(starting_letter_as_num, finishing_letter_as_num + 1):
        for last_letter in range(starting_letter_as_num, finishing_letter_as_num + 1):
            if first_letter == skipping_letter_as_num \
                    or skipping == skipping_letter_as_num \
                    or last_letter == skipping_letter_as_num:
                continue
            letter_first = chr(first_letter)
            letter_second = chr(skipping)
            letter_last = chr(last_letter)
            combination += 1
            print(f"{letter_first}{letter_second}{letter_last}", end=" ")
print(combination)
