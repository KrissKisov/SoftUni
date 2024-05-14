num_of_elements = int(input())
elements = set()

for i in range(num_of_elements):
    for element in input().split():
        elements.add(element)

print(*elements, sep='\n')
