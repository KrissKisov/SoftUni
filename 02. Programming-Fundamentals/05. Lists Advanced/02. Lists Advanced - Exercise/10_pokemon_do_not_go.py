integers = list(map(int, input().split()))
sum_of_removed = 0
while len(integers) > 0:
    index = int(input())
    if index < 0:
        index = 0
        element_to_remove = integers[index]
        integers = [(x + element_to_remove) if x <= integers[index] else (x - element_to_remove) for x in integers]
        integers[0] = integers[-1]
        sum_of_removed += element_to_remove

    elif index > len(integers) - 1:
        index = len(integers) - 1
        element_to_remove = integers[index]
        integers = [(x + element_to_remove) if x <= integers[index] else (x - element_to_remove) for x in integers]
        integers[-1] = integers[0]
        sum_of_removed += element_to_remove

    else:  # index in range(0, len(integers))
        element_to_remove = integers[index]
        integers = [(x + element_to_remove) if x <= element_to_remove else (x - element_to_remove) for x in integers]
        integers.pop(index)
        sum_of_removed += element_to_remove

print(sum_of_removed)
