# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     def __init__(self, fuel_quantity: float, fuel_consumption: float):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance: float) -> None:
#         ...
#
#     @abstractmethod
#     def refuel(self, fuel: float) -> None:
#         ...
#
#
# class Car(Vehicle):
#     AIR_CON_ON = 0.9
#
#     def drive(self, distance: float) -> None:
#         current_consumption = (self.fuel_consumption + self.AIR_CON_ON) * distance
#
#         if self.fuel_quantity >= current_consumption:
#             self.fuel_quantity -= current_consumption
#
#     def refuel(self, fuel: float) -> None:
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle):
#     AIR_CON_ON = 1.6
#     ACTUAL_TANK_VOLUME = 0.95
#
#     def drive(self, distance: float) -> None:
#         current_consumption = (self.fuel_consumption + self.AIR_CON_ON) * distance
#
#         if self.fuel_quantity >= current_consumption:
#             self.fuel_quantity -= current_consumption
#
#     def refuel(self, fuel: float) -> None:
#         self.fuel_quantity += fuel * self.ACTUAL_TANK_VOLUME

from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def air_con_on(self) -> float:
        pass

    def drive(self, distance: float) -> None:
        current_consumption = (self.fuel_consumption + self.air_con_on) * distance

        if self.fuel_quantity >= current_consumption:
            self.fuel_quantity -= current_consumption

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):

    @property
    def air_con_on(self) -> float:
        return 0.9

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ACTUAL_TANK_VOLUME = 0.95

    @property
    def air_con_on(self) -> float:
        return 1.6

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.ACTUAL_TANK_VOLUME


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
