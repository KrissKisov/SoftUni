from typing import List, Type
from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def food_that_can_eat(self) -> List[Type[Meat]]:
        return [Meat]

    @property
    def weight_to_gain(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_can_eat(self) -> List[Type[Meat] or Type[Vegetable] or Type[Fruit] or Type[Seed]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_to_gain(self) -> float:
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
