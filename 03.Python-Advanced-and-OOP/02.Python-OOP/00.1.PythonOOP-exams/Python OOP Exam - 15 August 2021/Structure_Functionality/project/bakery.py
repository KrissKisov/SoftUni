from typing import List, Tuple
from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:

    possible_food_types = {"Bread": Bread, "Cake": Cake}
    possible_drink_types = {"Tea": Tea, "Water": Water}
    possible_table_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income: float = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> str or None:

        if next((f for f in self.food_menu if f.name == name), None):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.possible_food_types:
            food = self.possible_food_types[food_type](name, price)

            if food:
                self.food_menu.append(food)

                return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> str or None:

        if next((d for d in self.drinks_menu if d.name == name), None):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.possible_drink_types:
            drink = self.possible_drink_types[drink_type](name, portion, brand)

            if drink:
                self.drinks_menu.append(drink)

                return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str or None:

        if next((t for t in self.tables_repository if t.table_number == table_number), None):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.possible_table_types:
            table = self.possible_table_types[table_type](table_number, capacity)

            if table:
                self.tables_repository.append(table)

                return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        available_tables = []
        for t in self.tables_repository:
            if not t.is_reserved and t.capacity >= number_of_people:
                available_tables.append(t)

        if not available_tables:
            return f"No available table for {number_of_people} people"

        table = available_tables[0]
        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: Tuple[str]) -> str:
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)

        if not table:
            return f"Could not find table {table_number}"

        available_foods = [f"Table {table_number} ordered:"]
        non_available_foods = [f"{self.name} does not have in the menu:"]
        for food_name in food_names:
            food = next((f for f in self.food_menu if f.name == food_name), None)
            if food:
                table.order_food(food)
                available_foods.append(food.__repr__())

            else:
                non_available_foods.append(food_name)

        message = available_foods + non_available_foods

        return "\n".join(message)

    def order_drink(self, table_number: int, *drink_names: Tuple[str]) -> str:
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)

        if not table:
            return f"Could not find table {table_number}"

        available_drinks = [f"Table {table_number} ordered:"]
        non_available_drinks = [f"{self.name} does not have in the menu:"]
        for drink_name in drink_names:
            drink = next((d for d in self.drinks_menu if d.name == drink_name), None)
            if drink:
                table.order_drink(drink)
                available_drinks.append(drink.__repr__())

            else:
                non_available_drinks.append(drink_name)

        message = available_drinks + non_available_drinks

        return "\n".join(message)

    def leave_table(self, table_number: int) -> str or None:

        table = next((t for t in self.tables_repository if t.table_number == table_number), None)

        if table:
            table_bill = table.get_bill()
            table.clear()
            self.total_income += table_bill

            return (f"Table: {table_number}\n"
                    f"Bill: {table_bill :.2f}")

    def get_free_tables_info(self) -> str or None:

        return "\n".join([t.free_table_info() for t in self.tables_repository])

    def get_total_income(self):

        return f"Total income: {self.total_income :.2f}lv"
