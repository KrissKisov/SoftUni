def perfect_number(some_number: int) -> bool:
    aliquot_sum = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            aliquot_sum += num
    if some_number == aliquot_sum:
        return True
    return False


number = int(input())
is_number_perfect = perfect_number(number)
if is_number_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
