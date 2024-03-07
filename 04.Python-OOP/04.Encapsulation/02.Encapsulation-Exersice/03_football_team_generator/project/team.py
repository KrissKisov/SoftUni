from typing import List, Union
from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:

        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)

        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> Union[str, Player]:

        for index, player in enumerate(self.__players):

            if player.name == player_name:

                return self.__players.pop(index)

        return f"Player {player_name} not found"
