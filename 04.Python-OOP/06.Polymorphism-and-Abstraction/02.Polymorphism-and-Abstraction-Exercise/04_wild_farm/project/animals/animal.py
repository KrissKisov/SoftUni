from abc import ABC, abstractmethod
from typing import List, Type
from project.food import Meat, Vegetable, Fruit, Seed, Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: float = 0

    @property
    @abstractmethod
    def food_that_can_eat(self) -> List[Type[Meat] or Type[Vegetable] or Type[Fruit] or Type[Seed]]:
        ...

    @property
    @abstractmethod
    def weight_to_gain(self) -> float:
        ...

    @staticmethod
    @abstractmethod
    def make_sound():
        ...

    def feed(self, food: Food) -> str or None:
        if type(food) not in self.food_that_can_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.weight_to_gain * food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
