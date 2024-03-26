from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_default_fuel_consumption_is_correct_value(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_not_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduce_fuel_after_driving(self):
        expected = 87.5

        self.vehicle.drive(10)

        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raises_exception(self):
        self.vehicle.fuel = 50

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_amount_fuel_increases_fuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(30)

        self.assertEqual(80, self.vehicle.fuel)

    def test_str_method_returns_correct_message(self):
        self.assertEqual(
            "The vehicle has 100 horse power with 100 fuel left and 1.25 fuel consumption",
            self.vehicle.__str__()
        )


if __name__ == "__main__":
    main()
