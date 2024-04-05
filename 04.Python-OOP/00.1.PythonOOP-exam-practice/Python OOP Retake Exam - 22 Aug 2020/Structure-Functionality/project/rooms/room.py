from typing import List
# from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0
        self.room_cost = None

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args) -> None:
        total_expenses = sum([(e.cost * 30) for el in args for e in el])

        # total_expenses = 0
        # for el_list in args:
        #     for el in el_list:
        #         if isinstance(el, Child):
        #             total_expenses += el.cost * 30
        #         elif isinstance(el, Appliance):
        #             total_expenses += el.get_monthly_expense()

        self.expenses = total_expenses
