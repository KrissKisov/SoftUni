from project.car.car import Car


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car: Car = None
        self.number_of_wins: int = 0  # increases with each won race

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")

        self.__name = value
