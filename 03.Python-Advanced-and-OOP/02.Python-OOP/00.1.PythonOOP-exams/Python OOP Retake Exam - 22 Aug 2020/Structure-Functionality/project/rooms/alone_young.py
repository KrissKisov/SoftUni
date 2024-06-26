from typing import List
from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances: List[Appliance] = [TV()]
        self.calculate_expenses(self.appliances)
