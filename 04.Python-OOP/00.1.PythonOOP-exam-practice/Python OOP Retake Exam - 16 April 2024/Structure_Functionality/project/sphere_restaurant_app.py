from typing import List
from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    valid_waiter_types = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    valid_client_types = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:

        if waiter_type not in self.valid_waiter_types:
            return f"{waiter_type} is not a recognized waiter type."

        if next((w for w in self.waiters if w.name == waiter_name), None):
            return f"{waiter_name} is already on the staff."

        waiter = self.valid_waiter_types[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str) -> str:

        if client_type not in self.valid_client_types:
            return f"{client_type} is not a recognized client type."

        if next((c for c in self.clients if c.name == client_name), None):
            return f"{client_name} is already a client."

        client = self.valid_client_types[client_type](client_name)
        self.clients.append(client)

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)

        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)

        if not client:
            return f"{client_name} is not a registered client."

        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)

        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        return f"{client_name} received a {client.apply_discount()[0]}% discount. Remaining points {client.points}"

    def generate_report(self):
        total_earnings_amount = sum(w.calculate_earnings() for w in self.waiters)
        total_unused_points = sum(c.points for c in self.clients)
        sorted_waiters = sorted(self.waiters, key=lambda x: -x.calculate_earnings())

        return (f"$$ Monthly Report $$\n"
                f"Total Earnings: ${total_earnings_amount :.2f}\n"
                f"Total Clients Unused Points: {total_unused_points}\n"
                f"Total Clients Count: {len(self.clients)}\n"
                f"** Waiter Details **\n") + "\n".join([w.__str__() for w in sorted_waiters])
