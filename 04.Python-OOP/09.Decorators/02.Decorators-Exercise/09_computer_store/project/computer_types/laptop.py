from project.computer_types.computer import Computer
from typing import Dict


class Laptop(Computer):

    @property
    def type_computer(self) -> str:
        return "laptop"

    @property
    def available_processor(self) -> Dict[str, int]:
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    @property
    def max_ram(self) -> int:
        return 64
