from typing import List
from project.band_members.musician import Musician


class Guitarist(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def can_learn_skills(self) -> List[str]:
        return ["play metal", "play rock", "play jazz"]
