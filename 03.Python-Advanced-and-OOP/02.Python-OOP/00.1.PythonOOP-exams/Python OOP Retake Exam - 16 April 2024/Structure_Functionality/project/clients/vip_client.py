from project.clients.base_client import BaseClient


class VIPClient(BaseClient):

    minimum_spent_per_point = 5

    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float) -> int:

        earned_points = int(order_amount / self.minimum_spent_per_point)
        self.points += earned_points

        return earned_points
