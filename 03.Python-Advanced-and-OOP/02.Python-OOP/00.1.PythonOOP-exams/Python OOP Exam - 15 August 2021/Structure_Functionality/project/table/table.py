from abc import ABC, abstractmethod
from typing import List
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int) -> None:

        if self.capacity >= number_of_people:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        orders = self.food_orders + self.drink_orders
        bill = sum(el.price for el in orders)

        return bill

    def clear(self) -> None:
        self.food_orders.clear()
        self.drink_orders.clear()
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self) -> str or None:
        if not self.is_reserved:
            return (f"Table: {self.table_number}\n"
                    f"Type: {self.__class__.__name__}\n"
                    f"Capacity: {self.capacity}")
