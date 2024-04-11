from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.cr = ClimbingRobot("Alpine", "part", 100, 100)
        self.cr2 = ClimbingRobot("Alpine", "part", 100, 100)

        self.cr2.installed_software = [{"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 50},
                                       {"name": "VSCode", "capacity_consumption": 49, "memory_consumption": 49}]

    def test_correct_init(self):
        self.assertEqual("Alpine", self.cr.category)
        self.assertEqual("part", self.cr.part_type)
        self.assertEqual(100, self.cr.capacity)
        self.assertEqual(100, self.cr.memory)
        self.assertEqual([], self.cr.installed_software)
        self.assertEqual(
            [{"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 50},
             {"name": "VSCode", "capacity_consumption": 49, "memory_consumption": 49}],
            self.cr2.installed_software
        )

    def test_category_setter_with_invalid_category_value_raises_value_error(self):
        expected = f"Category should be one of {self.ALLOWED_CATEGORIES}"

        with self.assertRaises(ValueError) as ve:
            self.cr.category = "Outdoor"

        self.assertEqual(expected, str(ve.exception))

    def test_category_setter_with_valid_category_expect_success(self):
        self.cr.category = "Indoor"

        self.assertEqual("Indoor", self.cr.category)

    def test_get_used_capacity_expect_success(self):#???
        self.cr.installed_software = []
        self.assertEqual(0, self.cr.get_used_capacity())

        self.cr2.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "VSCode", "capacity_consumption": 49, "memory_consumption": 51}
        ]

        expected_result = sum(s['capacity_consumption'] for s in self.cr2.installed_software)
        result = self.cr2.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity(self):
        expected = self.cr2.capacity - sum(s['capacity_consumption'] for s in self.cr2.installed_software)
        result = self.cr2.get_available_capacity()

        self.assertEqual(expected, result)

    def test_get_used_memory(self):
        expected = sum(s['memory_consumption'] for s in self.cr2.installed_software)
        result = self.cr2.get_used_memory()

        self.assertEqual(expected, result)

    def test_get_available_memory(self):
        expected = self.cr2.memory - sum(s['memory_consumption'] for s in self.cr2.installed_software)
        result = self.cr2.get_available_memory()

        self.assertEqual(expected, result)

    def test_install_software_with_max_equal_values_expect_success(self):

        software = {"name": "Pycharm", "capacity_consumption": 100, "memory_consumption": 100}
        expected = f"Software '{software['name']}' successfully installed on {self.cr.category} part."
        result = self.cr.install_software(software)

        self.assertEqual(expected, result)
        self.assertEqual([software], self.cr.installed_software)

    def test_install_software_with_less_than_max_values_expect_success(self):

        software = {"name": "Pycharm", "capacity_consumption": 80, "memory_consumption": 80}
        expected = f"Software '{software['name']}' successfully installed on {self.cr.category} part."
        result = self.cr.install_software(software)

        self.assertEqual(expected, result)
        self.assertEqual([software], self.cr.installed_software)

    def test_install_software_with_not_enough_available_capacity(self):

        software = {"name": "Pycharm", "capacity_consumption": 200, "memory_consumption": 80}

        expected = f"Software '{software['name']}' cannot be installed on {self.cr.category} part."
        result = self.cr.install_software(software)

        self.assertEqual(expected, result)
        self.assertEqual([], self.cr.installed_software)

    def test_install_software_with_not_enough_available_memory(self):

        software = {"name": "Pycharm", "capacity_consumption": 80, "memory_consumption": 200}
        expected = f"Software '{software['name']}' cannot be installed on {self.cr.category} part."
        result = self.cr.install_software(software)

        self.assertEqual(expected, result)
        self.assertEqual([], self.cr.installed_software)

    def test_install_software_with_not_enough_available_memory_and_capacity(self):

        software = {"name": "Linux", "capacity_consumption": 200, "memory_consumption": 200}
        expected = f"Software '{software['name']}' cannot be installed on {self.cr.category} part."
        result = self.cr.install_software(software)

        self.assertEqual(expected, result)
        self.assertEqual([], self.cr.installed_software)


if __name__ == "__main__":
    main()
