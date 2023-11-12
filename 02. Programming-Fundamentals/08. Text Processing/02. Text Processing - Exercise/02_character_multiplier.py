first_string, second_string = input().split()
shorter_string = ""
longer_string = ""
total_sum = 0
remaining_indexes_start = 0

if len(first_string) != len(second_string):
    shorter_string = min(first_string, second_string, key=len)
    longer_string = max(first_string, second_string, key=len)
else:
    shorter_string = first_string
    longer_string = second_string

for index in range(len(shorter_string)):
    remaining_indexes_start = index
    first_multiplier = ord(shorter_string[index])
    second_multiplier = ord(longer_string[index])
    total_sum += first_multiplier * second_multiplier
for index in range(remaining_indexes_start + 1, len(longer_string)):
    total_sum += ord(longer_string[index])

print(total_sum)
