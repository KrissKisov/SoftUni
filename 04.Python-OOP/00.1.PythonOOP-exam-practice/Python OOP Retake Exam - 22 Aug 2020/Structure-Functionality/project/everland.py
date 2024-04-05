from typing import List
from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        total_consumption = sum((r.expenses + r.room_cost) for r in self.rooms)

        return f"Monthly consumption: {total_consumption :.2f}$."

    def pay(self) -> str:
        message = ""
        for r in self.rooms:
            if r.budget >= (r.expenses + r.room_cost):
                r.budget -= (r.expenses + r.room_cost)
                message += f"{r.family_name} paid {r.expenses + r.room_cost :.2f}$ and have {r.budget :.2f}$ left.\n"

            else:
                message += f"{r.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(r)

        return message[:-1]

    def status(self) -> str:
        output = f"Total population: {sum(r.members_count for r in self.rooms)}\n"

        for room in self.rooms:
            output += (f"{room.family_name} with {room.members_count} members. "
                       f"Budget: {room.budget :.2f}$, Expenses: {room.expenses :.2f}$\n")

            if room.children:

                for num, child in enumerate(room.children):
                    output += f"--- Child {num + 1} monthly cost: {child.cost * 30 :.2f}$\n"

            if hasattr(room, "appliances"):
                output += f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in room.appliances) :.2f}$\n"

        return output[:-1]
