class vowels:
    VOWELS = ["a", "e", "i", "u", "y", "o"]

    def __init__(self, string: str):
        self.string = string
        self.vowels_in_string = [v for v in self.string if v.lower() in vowels.VOWELS]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        self.index += 1

        if self.index >= len(self.vowels_in_string):
            raise StopIteration

        return self.vowels_in_string[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
