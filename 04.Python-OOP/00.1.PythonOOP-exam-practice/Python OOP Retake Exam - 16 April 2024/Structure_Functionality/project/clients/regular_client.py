from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    minimum_spent_per_point = 10

    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float) -> int:

        earned_points = int(order_amount / self.minimum_spent_per_point)
        self.points += earned_points

        return earned_points
