from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.td = TruckDriver("Driver", 1.0)

    def test_correct_init(self):
        self.assertEqual("Driver", self.td.name)
        self.assertEqual(1.0, self.td.money_per_mile)
        self.assertEqual({}, self.td.available_cargos)
        self.assertEqual(0, self.td.earned_money)
        self.assertEqual(0, self.td.miles)

    def test_earned_money_setter_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.td.earned_money = -1

        self.assertEqual(f"{self.td.name} went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_offer_already_in_the_dict_raises_error(self):
        self.td.available_cargos = {"Sofia": 100}

        with self.assertRaises(Exception) as ex:
            self.td.add_cargo_offer("Sofia", 50)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_expect_success(self):
        self.td.available_cargos = {"Sofia": 100}

        result = self.td.add_cargo_offer("Varna", 500)
        expected = f"Cargo for {500} to {'Varna'} was added as an offer."

        self.assertEqual({"Sofia": 100, "Varna": 500}, self.td.available_cargos)
        self.assertEqual(expected, result)

    def test_drive_best_cargo_offer_without_available_offers_raises_error(self):
        result = self.td.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_drive_best_offer_expect_success(self):
        self.td.available_cargos = {"Sofia": 100, "Varna": 50}

        expected = f"{self.td.name} is driving 100 to Sofia."
        result = self.td.drive_best_cargo_offer()

        self.assertEqual(expected, result)
        self.assertEqual(100.0, self.td.earned_money)
        self.assertEqual(100, self.td.miles)
        self.assertEqual(100, self.td.earned_money)

    def test_check_for_activities(self):
        self.td.money_per_mile = 10.0
        self.td.available_cargos = {"Sofia": 10000, "Varna": 500}
        self.td.drive_best_cargo_offer()
        self.td.check_for_activities(1000)

        self.assertEqual(88125.0, self.td.earned_money)

    def test_repr(self):
        self.td.available_cargos = {"Sofia": 100, "Varna": 50}
        self.td.drive_best_cargo_offer()

        expected = f"Driver has 100 miles behind his back."
        result = self.td.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
