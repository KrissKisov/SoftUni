from project.car.car import Car


class SportsCar(Car):

    @property
    def min_speed_limit(self) -> int:
        return 400

    @property
    def max_speed_limit(self) -> int:
        return 600
