def genrange(start: int, end: int):
    yield from range(start, end + 1)
    # num = start
    #
    # while num <= end:
    #     yield num
    #     num += 1


print(list(genrange(1, 10)))