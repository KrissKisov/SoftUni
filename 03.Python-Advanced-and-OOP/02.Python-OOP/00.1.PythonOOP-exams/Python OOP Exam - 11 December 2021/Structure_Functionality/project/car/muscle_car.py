from project.car.car import Car


class MuscleCar(Car):

    @property
    def min_speed_limit(self) -> int:
        return 250

    @property
    def max_speed_limit(self) -> int:
        return 450
