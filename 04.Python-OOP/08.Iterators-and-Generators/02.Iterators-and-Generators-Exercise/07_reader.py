def read_next(*args):

    for iterable in args:
        yield from iterable
        # for el in iterable:
        #     yield el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print()

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
