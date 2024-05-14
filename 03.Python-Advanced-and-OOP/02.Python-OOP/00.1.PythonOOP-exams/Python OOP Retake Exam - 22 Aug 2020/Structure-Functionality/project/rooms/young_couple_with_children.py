from typing import List
from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, (salary_one + salary_two), (2 + len(children)))
        self.children: List[Child] = list(children)
        self.room_cost = 30
        self.appliances: List[Appliance] = [TV(), Fridge(), Laptop()] * (2 + len(self.children))
        self.calculate_expenses(self.appliances, self.children)
