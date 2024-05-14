from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.r = Restaurant("Restaurant", 2)

    def test_correct_init(self):
        self.assertEqual("Restaurant", self.r.name)
        self.assertEqual(2, self.r.capacity)
        self.assertEqual([], self.r.waiters)

    def test_name_setter_with_invalid_string_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.r.name = "     "

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_setter_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r.capacity = -1

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters(self):
        self.r.waiters = [{"name": "Ivan", "total_earnings": 10}, {"name": "Peter", "total_earnings": 5}]

        expected = [{"name": "Peter", "total_earnings": 5}]
        result = self.r.get_waiters(1, 8)

        self.assertEqual(expected, result)

    def test_add_waiter_with_no_capacity_for_it_returns_correct_message(self):
        self.r.waiters = [{"name": "Ivan"}, {"name": "Peter"}]

        expected = "No more places!"
        result = self.r.add_waiter("George")

        self.assertEqual([{"name": "Ivan"}, {"name": "Peter"}], self.r.waiters)
        self.assertEqual(expected, result)

    def test_add_waiter_with_existing_waiter_return_correct_message(self):
        self.r.waiters = [{"name": "Ivan"}]

        expected = "The waiter Ivan already exists!"
        result = self.r.add_waiter("Ivan")

        self.assertEqual([{"name": "Ivan"}], self.r.waiters)
        self.assertEqual(expected, result)

    def test_add_waiter_expect_success(self):
        self.r.waiters = [{"name": "Ivan"}]

        expected = "The waiter Peter has been added."
        result = self.r.add_waiter("Peter")

        self.assertEqual([{"name": "Ivan"}, {"name": "Peter"}], self.r.waiters)
        self.assertEqual(expected, result)

    def test_remove_waiter_with_non_existing_name_returns_correct_message(self):
        self.r.waiters = [{"name": "Ivan"}, {"name": "Peter"}]

        expected = "No waiter found with the name George."
        result = self.r.remove_waiter("George")

        self.assertEqual([{"name": "Ivan"}, {"name": "Peter"}], self.r.waiters)
        self.assertEqual(expected, result)

    def test_remove_waiter_expect_success(self):
        self.r.waiters = [{"name": "Ivan"}, {"name": "Peter"}]

        expected = "The waiter Ivan has been removed."
        result = self.r.remove_waiter("Ivan")

        self.assertEqual([{"name": "Peter"}], self.r.waiters)
        self.assertEqual(expected, result)

    def test_get_total_earnings(self):
        self.r.waiters = [{"name": "Ivan", "total_earnings": 10}, {"name": "Peter", "total_earnings": 5}]

        result = self.r.get_total_earnings()

        self.assertEqual(15, result)


if __name__ == "__main__":
    main()
