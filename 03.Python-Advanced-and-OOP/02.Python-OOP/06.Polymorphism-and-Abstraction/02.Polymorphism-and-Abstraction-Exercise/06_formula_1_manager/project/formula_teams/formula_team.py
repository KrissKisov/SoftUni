from abc import ABC, abstractmethod

class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def expenses_per_race(self) -> int:
        ...

    @property
    @abstractmethod
    def sponsors(self) -> dict:
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue: int = 0

        for sponsor in self.sponsors.values():
            for position, reward in sponsor.items():
                if race_pos <= position:
                    revenue += reward
                    break

        revenue -= self.expenses_per_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
