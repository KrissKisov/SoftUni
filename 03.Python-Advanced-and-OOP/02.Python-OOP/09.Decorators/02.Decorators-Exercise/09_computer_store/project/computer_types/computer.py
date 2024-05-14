from abc import ABC, abstractmethod
from math import log2
from typing import Optional, Dict


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: Optional[str] = None
        self.ram: Optional[int] = None
        self.price: int = 0

    @property
    @abstractmethod
    def type_computer(self) -> str:
        ...

    @property
    @abstractmethod
    def available_processor(self) -> Dict[str, int]:
        ...

    @property
    @abstractmethod
    def max_ram(self) -> int:
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def valid_ram(num: int):
        result = log2(num)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processor:
            raise ValueError(f"{processor} is not compatible with {self.type_computer} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.valid_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_computer} {self.manufacturer} {self.model}!")

        processor_price = self.available_processor[processor]
        ram_price = int(log2(ram)) * 100
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
