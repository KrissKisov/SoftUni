from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):

    PROTECTION = 90
    PRICE = 25.0
    INCREASE_OF_PRICE = 1.1

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self) -> None:
        self.price *= self.INCREASE_OF_PRICE
