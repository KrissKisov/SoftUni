from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Mazda6",
                                 "family",
                                 50_000,
                                 5_000.0)

    def test_correct_init(self):
        self.assertEqual("Mazda6", self.car.model)
        self.assertEqual("family", self.car.car_type)
        self.assertEqual(50_000, self.car.mileage)
        self.assertEqual(5000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_with_invalid_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_setter_with_invalid_amount_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!",
                         str(ve.exception))

    def test_promotional_price_with_amount_equal_to_actual_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5000.0)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_promotional_price_with_amount_less_than_actual_price_expect_success(self):
        result = self.car.set_promotional_price(3_000.0)

        self.assertEqual(3000.0, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_need_repair_with_amount_too_high_does_not_change_price(self):
        result = self.car.need_repair(2500.1, "Need new engine!")

        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.assertEqual("Repair is impossible!", result)

    def test_need_repair_with_smaller_amount_change_price(self):
        result = self.car.need_repair(2000, "Need new engine!")

        self.assertEqual(7000, self.car.price)
        self.assertEqual(["Need new engine!"], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

    def test__gt__with_different_type_of_car_returns_correct_message(self):
        self.other = SecondHandCar("Mazda RX-7", "sports", 30_000, 10_000)

        result = self.car.__gt__(self.other)

        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__with_same_type_of_car_with_higher_price_returns_false(self):
        self.other = SecondHandCar("Insignia", "family", 50_000, 10_000)

        result = self.car.__gt__(self.other)

        self.assertFalse(result)
        self.assertEqual(False, result)

    def test__gt__with_same_type_of_car_with_smaller_price_returns_true(self):
        self.other = SecondHandCar("Insignia", "family", 50_000, 4_000)

        result = self.car.__gt__(self.other)

        self.assertTrue(result)
        self.assertEqual(True, result)

    def test_str_method_returns_correct_message(self):

        self.car.need_repair(600, "Need new wheels!")

        expected = """Model Mazda6 | Type family | Milage 50000km
Current price: 5600.00 | Number of Repairs: 1"""
        result = self.car.__str__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
