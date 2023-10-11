given_numbers = list(map(float, input().split()))
# rounded_numbers = []
# for number in given_numbers:
#     rounded_numbers.append(round(number))
rounded_numbers = [round(num) for num in given_numbers]
print(rounded_numbers)
