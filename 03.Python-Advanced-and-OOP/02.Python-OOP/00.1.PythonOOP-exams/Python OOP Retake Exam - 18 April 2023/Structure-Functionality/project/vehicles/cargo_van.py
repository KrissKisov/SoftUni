from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float) -> None:

        percentage = round(mileage / self.max_mileage * 100)
        additional_percent = 5

        self.battery_level -= (percentage + additional_percent)
