clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
number_of_racks = 1
current_rack = 0
while clothes_stack:
    current_garment = clothes_stack.pop()
    if rack_capacity >= current_rack + current_garment:
        current_rack += current_garment

    else:
        number_of_racks += 1
        current_rack = 0
        current_rack += current_garment

print(number_of_racks)
