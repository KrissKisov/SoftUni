from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    valid_car_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str or None:

        if car_type in self.valid_car_types:
            car_exists = next((c for c in self.cars if c.model == model), None)

            if car_exists:
                raise Exception(f"Car {model} is already created!")

            car = self.valid_car_types[car_type](model, speed_limit)
            self.cars.append(car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:

        if next((d for d in self.drivers if d.name == driver_name), None):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:

        if next((r for r in self.races if r.name == race_name), None):
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:

        needed_type_cars = [c for c in self.cars if c.__class__.__name__ == car_type]
        available_cars = [c for c in needed_type_cars if not c.is_taken]
        driver = next((d for d in self.drivers if d.name == driver_name), None)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")

        car = available_cars[-1]

        if driver.car:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False

            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:

        race = next((r for r in self.races if r.name == race_name), None)
        driver = next((d for d in self.drivers if d.name == driver_name), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if next((d for d in race.drivers if d.name == driver.name), None):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next((r for r in self.races if r.name == race_name), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_cars = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        message = []
        for driver in sorted_cars[:3]:
            driver.number_of_wins += 1
            message.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(message)
