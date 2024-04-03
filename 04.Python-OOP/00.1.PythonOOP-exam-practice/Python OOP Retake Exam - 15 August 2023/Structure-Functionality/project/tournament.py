from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str) -> str:
        try:
            current_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(current_equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:

        try:
            current_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        self.teams.append(current_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:

        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        try:
            team = [t for t in self.teams if t.name == team_name][0]
        except IndexError:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:

        number_of_changed_equipment = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str) -> str:

        first_team = next((t for t in self.teams if t.name == team_name1), None)
        second_team = next((t for t in self.teams if t.name == team_name2), None)

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_results = first_team.advantage + sum([e.protection for e in first_team.equipment])
        second_team_results = second_team.advantage + sum([e.protection for e in second_team.equipment])

        if first_team_results > second_team_results:
            first_team.win()
            return f"The winner is {first_team.name}."

        elif first_team_results < second_team_results:
            second_team.win()
            return f"The winner is {second_team.name}."

        return "No winner in this game."

    def get_statistics(self) -> str:

        teams = sorted(self.teams, key=lambda t: -t.wins)
        message = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", f"Teams:"]
        [message.append(t.get_statistics()) for t in teams]

        return "\n".join(message)
