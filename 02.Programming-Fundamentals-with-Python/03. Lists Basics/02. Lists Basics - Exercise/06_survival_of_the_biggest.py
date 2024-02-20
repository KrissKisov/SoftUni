integers_as_string = input().split()
numbers_to_remove = int(input())
list_as_integers = list(map(int, integers_as_string))

for number in range(numbers_to_remove):
    list_as_integers.remove(min(list_as_integers))
print(", ".join(str(number) for number in list_as_integers))
