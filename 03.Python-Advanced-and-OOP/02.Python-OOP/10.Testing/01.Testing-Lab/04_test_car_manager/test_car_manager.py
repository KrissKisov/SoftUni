from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Mazda", "Mazda6", 6, 65)

    def test_correct_init(self):
        self.assertEqual("Mazda", self.car.make)
        self.assertEqual("Mazda6", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_raise_exception_when_make_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_raise_exception_when_model_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_raise_exception_when_fuel_consumption_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_when_fuel_capacity_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_when_fuel_amount_is_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -7

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_raise_exception_when_refuel_method_is_called_with_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_when_called_with_value_bigger_than_capacity(self):
        expected = self.car.fuel_capacity
        self.car.refuel(75)

        self.assertEqual(expected, self.car.fuel_amount)

    def test_drive_bigger_distance_than_possible_with_available_fuel_raise_exception(self):
        self.car.fuel_amount = 5

        with self.assertRaises(Exception) as ex:
            self.car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_reduce_fuel_amount(self):
        self.car.fuel_amount = 10
        expected = 4

        self.car.drive(100)

        self.assertEqual(expected, self.car.fuel_amount)

if __name__ == "__main__":
    main()
