def filling_electrons(some_electrons: int) -> list:
    shell = 0
    filled_shells = []
    while some_electrons > 0:
        shell += 1
        used_electrons = 2 * shell ** 2
        if some_electrons >= used_electrons:
            some_electrons -= used_electrons
            filled_shells.append(used_electrons)
        else:
            filled_shells.append(some_electrons)
            break
    return filled_shells


electrons = int(input())
print(filling_electrons(electrons))
