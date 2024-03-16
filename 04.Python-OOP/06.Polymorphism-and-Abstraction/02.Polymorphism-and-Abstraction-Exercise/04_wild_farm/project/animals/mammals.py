from typing import List, Type
from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):

    @property
    def food_that_can_eat(self) -> List[Type[Vegetable] or Type[Fruit]]:
        return [Vegetable, Fruit]

    @property
    def weight_to_gain(self) -> float:
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def food_that_can_eat(self) -> List[Type[Meat]]:
        return [Meat]

    @property
    def weight_to_gain(self) -> float:
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def food_that_can_eat(self) -> List[Type[Meat] or Type[Vegetable]]:
        return [Meat, Vegetable]

    @property
    def weight_to_gain(self) -> float:
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def food_that_can_eat(self) -> List[Type[Meat]]:
        return [Meat]

    @property
    def weight_to_gain(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
