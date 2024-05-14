class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iteration = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iteration += 1

        if self.iteration < self.number:
            return self.sequence[self.iteration % len(self.sequence)]

        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
