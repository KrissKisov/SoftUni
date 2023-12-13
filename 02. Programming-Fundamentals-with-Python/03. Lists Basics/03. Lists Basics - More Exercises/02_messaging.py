sequence_of_numbers = input().split()
given_string = input()
given_string_as_list = list(given_string)
final_message = []

for number in sequence_of_numbers:
    sum_of_digits = sum(map(int, number))
    current_string = given_string_as_list * (1 + sum_of_digits // len(given_string))
    for letter in range(len(current_string)):
        if letter == sum_of_digits:
            final_message.append(current_string[letter])
            given_string_as_list.remove(current_string[letter])
            break
            
print("".join(final_message))
