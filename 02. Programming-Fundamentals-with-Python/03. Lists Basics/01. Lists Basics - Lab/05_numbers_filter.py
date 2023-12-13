number_of_integers = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(number_of_integers):
    integer = int(input())
    if integer % 2 == 0:
        even_list.append(integer)
    else:
        odd_list.append(integer)

    if integer < 0:
        negative_list.append(integer)
    else:
        positive_list.append(integer)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)
