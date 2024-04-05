from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):

    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("123", "Education", 10, 100.0)
        self.robot2 = Robot("456", "Education", 10, 100.0)
        self.robot3 = Robot("789", "Education", 10, 100.0)

    def test_correct_init(self):
        self.assertEqual("123", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_with_invalid_category_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Worker"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_setter_with_invalid_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_component_already_in_hardware_upgrades_list_returns_correct_message(self):
        self.robot.hardware_upgrades = ["test", "test2"]

        result = self.robot.upgrade("test", 10.0)

        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)
        self.assertEqual(["test", "test2"], self.robot.hardware_upgrades)
        self.assertEqual(100.0, self.robot.price)

    def test_upgrade_with_new_component_expect_success(self):
        self.robot.hardware_upgrades = ["test", "test2"]

        result = self.robot.upgrade("test3", 10.0)

        self.assertEqual(["test", "test2", "test3"], self.robot.hardware_upgrades)
        self.assertEqual(115.0, self.robot.price)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with {"test3"}.', result)

    def test_update_with_enough_capacity_but_invalid_version(self):
        self.robot.software_updates = [5.0, 4.0]
        self.robot.available_capacity -= sum(self.robot.software_updates)

        result = self.robot.update(5.0, 1)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
        self.assertEqual([5.0, 4.0], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test_update_with_valid_version_but_not_enough_capacity(self):
        self.robot.software_updates = [5.0, 4.0]
        self.robot.available_capacity -= sum(self.robot.software_updates)

        result = self.robot.update(6.0, 2)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
        self.assertEqual([5.0, 4.0], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test_update_with_valid_version_and_enough_capacity_expect_success(self):
        self.robot.software_updates = [3.0, 4.0]
        self.robot.available_capacity -= sum(self.robot.software_updates)

        result = self.robot.update(5.0, 2)

        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version {5.0}.', result)
        self.assertEqual([3.0, 4.0, 5.0], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test__gt__method_returns_correct_message_with_equal_prices(self):
        expected = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.robot2.robot_id}.'
        result = self.robot.__gt__(self.robot2)

        self.assertEqual(expected, result)

    def test__gt__method_returns_correct_message_for_robots_with_different_prices(self):
        self.robot2.price = 50.0

        expected = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.robot2.robot_id}.'
        result = self.robot.__gt__(self.robot2)

        self.assertEqual(expected, result)

        self.robot3.price = 150.0

        expected = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.robot3.robot_id}.'
        result = self.robot.__gt__(self.robot3)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
