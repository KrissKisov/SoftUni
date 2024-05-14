class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iteration = 0
        self.number = -self.step

    def __iter__(self):
        return self

    def __next__(self):

        if self.iteration >= self.count:
            raise StopIteration

        self.number += self.step
        self.iteration += 1
        return self.number

    # # Correct but does not work for judge
    # def __iter__(self):
    #     return iter(range(0, self.count * self.step, self.step))


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
