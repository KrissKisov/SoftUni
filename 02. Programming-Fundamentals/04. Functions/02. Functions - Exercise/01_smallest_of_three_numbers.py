# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(min(first_number,second_number, third_number))

def smallest_number(list_of_numbers):
    return min(list_of_numbers)


numbers_list = [int(input()), int(input()), int(input())]
print(smallest_number(numbers_list))
