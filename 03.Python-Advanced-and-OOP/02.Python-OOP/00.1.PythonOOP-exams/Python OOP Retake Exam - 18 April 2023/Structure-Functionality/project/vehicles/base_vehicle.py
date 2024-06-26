from abc import ABC, abstractmethod
from project.validation import validate_parameter


class BaseVehicle(ABC):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = 100
        self.is_damaged: bool = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        validate_parameter(value, "Brand cannot be empty!")

        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        validate_parameter(value, "Model cannot be empty!")

        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        validate_parameter(value, "License plate number is required!")

        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float) -> None:
        ...

    def recharge(self) -> None:
        self.battery_level = 100

    def change_status(self) -> None:
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return (f"{self.brand} {self.model} License plate: {self.license_plate_number} "
                f"Battery: {self.battery_level}% Status: {'OK' if not self.is_damaged else 'Damaged'}")
